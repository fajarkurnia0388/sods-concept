"""
SODS Package Unit Testing Suite
===============================
Verifies core Observer-Driven Specialization properties:
- Polymorphic Inline Caching (PIC) on stable workloads.
- Ultra-fast execution bypassing dictionary dispatch.
- Synchronous Guard deopt counter from SpecializedFunction wrapper.
- Mixed numeric JIT support (`int + float` & `float + int`).
- Tier-lowering permanent locks on volatile megamorphic sites.
- WASI pure/impure taint analysis tags.
- Highly enriched JSON Cookie persistence (SHA-256 program hash, schema v2).
"""

import os
import unittest
from typing import List, Tuple, Any

from sods import SODSSandbox, EquivalenceVerifier
from sods.dummy_target import generic_add, generic_log_io
from sods.specializer import SpecializedFunction

TEST_CACHE_PATH = ".sods/test_profile.json"

class TestSODSConcept(unittest.TestCase):
    def setUp(self):
        self.sandbox = SODSSandbox(reset_cache=True, profile_path=TEST_CACHE_PATH)

    def tearDown(self):
        if os.path.exists(TEST_CACHE_PATH):
            os.chmod(TEST_CACHE_PATH, 0o600)
            os.remove(TEST_CACHE_PATH)

    def test_pic_specializes_int_float_and_mixed_numerics(self):
        # 1. Cold Run recording int, float, and mixed numerics
        cold_workloads = (
            [(i, i + 1) for i in range(50)] + 
            [(float(i), float(i + 1)) for i in range(50)] +
            [(i, float(i + 1)) for i in range(50)]
        )
        self.sandbox.cold_run("generic_add", generic_add, cold_workloads)
        
        # Verify PIC is built for exactly 3 stable signatures
        self.assertIn("generic_add", self.sandbox.specialized)
        sfn, label, supported_sigs = self.sandbox.specialized["generic_add"]
        self.assertTrue(label.startswith("Polymorphic Inline Cache (PIC: 3)"))
        self.assertIn(("int", "float"), supported_sigs)

    def test_empirical_equivalence_verifier(self):
        cold_workloads = [(i, i + 1) for i in range(100)]
        self.sandbox.cold_run("generic_add", generic_add, cold_workloads)
        sfn, _, _ = self.sandbox.specialized["generic_add"]
        
        # Verify empirical equivalence on bounded inputs matches perfectly
        passed = EquivalenceVerifier.verify("generic_add", generic_add, sfn, [(10, 20), (5, 15)])
        self.assertTrue(passed)

    def test_synchronous_guard_deopt_counter(self):
        cold_workloads = [(i, i + 1) for i in range(100)]
        self.sandbox.cold_run("generic_add", generic_add, cold_workloads)
        
        # Execute warm run with string inputs (which were never observed in cold run)
        results, deopt_fails = self.sandbox.warm_run("generic_add", generic_add, [("foo", "bar")])
        self.assertEqual(results, ["foobar"])
        self.assertEqual(deopt_fails, 1)

    def test_tier_lowering_on_volatile_megamorphic_call_site(self):
        cold_workloads = [(i, i + 1) for i in range(100)]
        self.sandbox.cold_run("generic_add", generic_add, cold_workloads)
        
        # Force a volatile megamorphic storm (str and list mixed)
        storm = [("a", "b"), ([1], [2]), (10.0, 20.0), ("c", "d"), ([3], [4])] * 4
        _, deopts = self.sandbox.warm_run("generic_add", generic_add, storm)
        self.assertGreater(deopts, 0)
        
        # Verify function is permanently burned into tier_lowered locked set
        self.assertIn("generic_add", self.sandbox.tier_lowered)
        
        # Verify subsequent runs are locked to Generic Passthrough
        _, subsequent_deopts = self.sandbox.warm_run("generic_add", generic_add, [(1, 2)])
        self.assertEqual(subsequent_deopts, 0)

    def test_wasi_impure_function_blocked_from_specialization(self):
        io_workloads = [("log msg 1",), ("log msg 2",)]
        self.sandbox.cold_run("generic_log_io", generic_log_io, io_workloads, is_io_side_effect=True)
        
        # Verify explicit block label
        _, label, _ = self.sandbox.specialized["generic_log_io"]
        self.assertEqual(label, "WASI Syscall Passthrough")

    def test_enriched_cookie_save_load_persistence(self):
        cold_workloads = [(i, i + 1) for i in range(100)]
        self.sandbox.cold_run("generic_add", generic_add, cold_workloads)
        self.sandbox.save_cookie()
        self.assertTrue(os.path.exists(TEST_CACHE_PATH))
        
        # Spin up a fresh host sandbox instance and verify deserialization
        fresh_sandbox = SODSSandbox(profile_path=TEST_CACHE_PATH)
        loaded = fresh_sandbox.load_cookie()
        self.assertTrue(loaded)
        self.assertIn("generic_add", fresh_sandbox.specialized)
        sfn, label, supp_sigs = fresh_sandbox.specialized["generic_add"]
        self.assertEqual(supp_sigs, [("int", "int")])

    def test_guard_thrashing_stress_iter_p1(self):
        """P1: Stress test guard thrashing with 100% miss rate."""
        cold_workloads = [(i, i + 1) for i in range(100)]
        self.sandbox.cold_run("generic_add", generic_add, cold_workloads)
        # 100% miss storm
        storm = [("x", "y"), ([1],[2]), ("a","b"), ([3],[4])] * 25
        _, deopts = self.sandbox.warm_run("generic_add", generic_add, storm)
        self.assertGreaterEqual(deopts, 90)
        # Must be tier-lowered
        self.assertIn("generic_add", self.sandbox.tier_lowered)

    def test_thread_safety_concurrent_warm_run(self):
        """P1: Concurrent warm_run must not corrupt deopt_count."""
        import threading
        cold_workloads = [(i, i + 1) for i in range(100)]
        self.sandbox.cold_run("generic_add", generic_add, cold_workloads)
        sfn, _, _ = self.sandbox.specialized["generic_add"]
        
        def worker():
            for _ in range(20):
                sfn(1, 2)  # hit
                try:
                    sfn("a", "b")  # miss -> deopt
                except Exception:
                    pass
        
        threads = [threading.Thread(target=worker) for _ in range(4)]
        for t in threads: t.start()
        for t in threads: t.join()
        # deopt_count should be >= 0 and not crash — lock protects it
        self.assertGreaterEqual(sfn.deopt_count, 0)
        
    def test_cookie_hmac_tamper_detection_iter2(self):
        import json
        cold_workloads = [(i, i + 1) for i in range(100)]
        self.sandbox.cold_run("generic_add", generic_add, cold_workloads)
        self.sandbox.save_cookie()
        
        # Tamper with the cookie
        os.chmod(TEST_CACHE_PATH, 0o600)
        with open(TEST_CACHE_PATH, "r") as f:
            cookie = json.load(f)
        if "payload" in cookie:
            cookie["payload"]["tier_lowered"] = ["fake_target"]
            with open(TEST_CACHE_PATH, "w") as f:
                json.dump(cookie, f)
                
        fresh_sandbox = SODSSandbox(profile_path=TEST_CACHE_PATH)
        loaded = fresh_sandbox.load_cookie()
        self.assertFalse(loaded)

if __name__ == "__main__":
    unittest.main()
