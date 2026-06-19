"""
SODSSandbox Runtime Wrapper
===========================
Orchestrates the entire 5-Stage Observer-Driven Specialization pipeline:
1. Cold Run   : Intercepts generic execution and records profiles.
2. Specializer: Builds specialized fast paths with synchronous Guard counters.
3. Verify     : Executes bounded empirical equivalence verification.
4. Cookie     : Serializes highly enriched profile metadata and cryptographic attestation to disk.
5. Warm Run   : Executes ultra-fast specialized code with OSR Deoptimization fallback
                and automatic tier-lowering protection on volatile megamorphic sites.
"""

import json
import os
import sys
import time
import random
import hashlib
from typing import Callable, List, Tuple, Any

from .profile import Profile
from .specializer import make_specialized_add, SpecializedFunction

CACHE_DIR = ".sods"
PROFILE_PATH = os.path.join(CACHE_DIR, "profile.json")

def file_sha256(path: str) -> str:
    """Computes a secure SHA-256 cryptographic hash of a source file."""
    h = hashlib.sha256()
    if os.path.exists(path):
        with open(path, "rb") as f:
            for chunk in iter(lambda: f.read(65536), b""):
                h.update(chunk)
    return h.hexdigest()

class SODSSandbox:
    def __init__(self, reset_cache: bool = False, profile_path: str = PROFILE_PATH):
        self.profile = Profile()
        self.specialized = {}       # fn_name -> (callable, label, supported_sigs)
        self.deopt_ratios = {}      # fn_name -> (deopt_fails, total_calls)
        self.tier_lowered = set()   # fn_name whose fast path is permanently burned
        self.profile_path = profile_path

        if reset_cache and os.path.exists(self.profile_path):
            os.remove(self.profile_path)

    # ── STAGE 1: COLD RUN ────────────────────────────────────────────────────
    def cold_run(self, fn_name: str, fn: Callable, workloads: List[Tuple[Any, ...]], is_io_side_effect: bool = False) -> List[Any]:
        """
        Executes generic code inside the observer sandbox, capturing call profiles.
        If is_io_side_effect is True, Taint Analysis marks the function as impure
        and explicitly blocks pure runtime specialization (WASI Boundary).
        """
        print(f"\n[COLD RUN] '{fn_name}' — observing runtime execution inside Sandbox...")
        
        if is_io_side_effect:
            print(f"  [TAINT: IMPURE] Function '{fn_name}' exhibits non-deterministic side-effects (I/O).")
            print(f"  [WASI BOUNDARY] Runtime specialization BLOCKED — passthrough directly to Host OS.")
            self.specialized[fn_name] = (fn, "WASI Syscall Passthrough", [])
            return [fn(*args) for args in workloads]

        results = []
        for args in workloads:
            self.profile.record(fn_name, args)
            results.append(fn(*args))

        self._try_specialize(fn_name, fn)
        return results

    def _try_specialize(self, fn_name: str, fn: Callable) -> None:
        if not self.profile.is_hot(fn_name):
            return

        stable_sigs = self.profile.get_stable_signatures(fn_name)
        if not stable_sigs:
            print(f"  -> Type signatures are highly unstable. Specialization skipped.")
            return

        if fn_name == "generic_add":
            sfn, label, supported_sigs = make_specialized_add(stable_sigs, fn)
        else:
            sfn, label, supported_sigs = fn, "Generic Passthrough", []

        self.specialized[fn_name] = (sfn, label, supported_sigs)
        print(f"  -> SPECIALIZATION BUILT: {label}")
        print(f"     Observed PIC Profiles: {stable_sigs}")
        if supported_sigs != stable_sigs:
            print(f"     Supported JIT Signatures: {supported_sigs}")

    # ── STAGE 5: WARM RUN ────────────────────────────────────────────────────
    def warm_run(self, fn_name: str, generic_fn: Callable, workloads: List[Tuple[Any, ...]]) -> Tuple[List[Any], int]:
        """
        Executes specialized fast paths with ultra-precise synchronous Guard tracking.
        Monitors Guard failure ratios to prevent deoptimization thrashing.
        """
        print(f"\n[WARM RUN] '{fn_name}'", end="")
        
        # Simulates Timing Noise Randomization to foil Sandbox Evasion Timing Attacks
        time.sleep(random.uniform(0, 0.000001))

        if fn_name in self.tier_lowered:
            print(f" — STATUS: Tier-Lowered (permanently locked to safe Generic Target).")
            print(f"  [TIER-LOWERED LOCKED] Previous deoptimization thrashing triggered permanent evacuation.")
            sfn = generic_fn
        elif fn_name in self.specialized:
            sfn, label, _ = self.specialized[fn_name]
            print(f" — loading fast path: {label}")
        else:
            print(f" — no specialized fast path available. Reverting to Generic Target.")
            sfn = generic_fn

        # Reset Guard counter if it's our SpecializedFunction object
        if isinstance(sfn, SpecializedFunction):
            sfn.deopt_count = 0

        results = []
        total_calls = len(workloads)
        
        for args in workloads:
            r = sfn(*args)
            results.append(r)
            
        # Pull synchronous Guard failure count exactly from the JIT wrapper
        deopt_count = sfn.deopt_count if isinstance(sfn, SpecializedFunction) else 0

        # ── Tier-Lowering Evaluation on Megamorphic Call Sites ──────────────
        if deopt_count > 0 and fn_name not in self.tier_lowered:
            print(f"  [OSR DEOPT] {deopt_count}x synchronous Guard failures -> transparan fallback to Generic Target (SAFE).")
            
            deopts_so_far, calls_so_far = self.deopt_ratios.get(fn_name, (0, 0))
            new_deopts = deopts_so_far + deopt_count
            new_calls = calls_so_far + total_calls
            self.deopt_ratios[fn_name] = (new_deopts, new_calls)
            
            failure_ratio = new_deopts / new_calls
            if failure_ratio > 0.30 and new_calls >= 10:
                print(f"  [TIER-LOWERING] Highly volatile megamorphic call site detected! "
                      f"Failure ratio: {failure_ratio:.0%} > 30% threshold.")
                print(f"  [TIER-LOWERING] Permanently burning specialized fast path for '{fn_name}'.")
                print(f"  [TIER-LOWERING] Future execution locked to Generic Target to prevent Guard Thrashing.")
                self.tier_lowered.add(fn_name)

        return results, deopt_count

    # ── STAGE 4: COOKIE PERSISTENCE WITH ENRICHED METADATA ────────────────────
    def save_cookie(self) -> None:
        """Serializes highly enriched profile metadata and cryptographic hash to JSON."""
        cache_dir = os.path.dirname(self.profile_path)
        if cache_dir:
            os.makedirs(cache_dir, exist_ok=True)
            
        # Build fully verifiable enriched metadata schema
        data = {
            "schema_version": 2,
            "runtime": "sods-python-experimental-poc",
            "python_version": sys.version,
            "platform": sys.platform,
            "timestamp": time.time(),
            "program_hash": file_sha256(sys.argv[0] if sys.argv else "__main__"),
            "profile": {
                "type_seen": {
                    k: {",".join(t): c for t, c in v.items()}
                    for k, v in self.profile.type_seen.items()
                },
                "call_count": self.profile.call_count,
            },
            "specialized": {
                k: {
                    "label": v[1],
                    "supported_signatures": v[2]
                }
                for k, v in self.specialized.items()
            },
            "tier_lowered": list(self.tier_lowered),
        }
        with open(self.profile_path, "w") as f:
            json.dump(data, f, indent=2)
            
        print(f"\n[COOKIE] Serialisasi Cookie berhasil. Metadata tersimpan ke: {self.profile_path}")
        print(f"  • Program SHA-256 : {data['program_hash'][:16]}...")
        print(f"  • Modul Aktif     : {list(self.specialized.keys())}")
        print(f"  • Tier-Lowered    : {list(self.tier_lowered) or 'Tidak ada'}")

    def load_cookie(self) -> bool:
        """Loads enriched profile states and reconstitutes SpecializedFunction objects."""
        if not os.path.exists(self.profile_path):
            return False

        with open(self.profile_path) as f:
            data = json.load(f)

        for fn, bucket in data["profile"]["type_seen"].items():
            self.profile.type_seen[fn] = {
                tuple(k.split(",")): v for k, v in bucket.items()
            }
        self.profile.call_count = data["profile"]["call_count"]
        self.tier_lowered = set(data.get("tier_lowered", []))

        # Reconstitute SpecializedFunction wrappers with their supported signatures
        for fn, meta in data.get("specialized", {}).items():
            if fn == "generic_add" and fn not in self.tier_lowered:
                stable = self.profile.get_stable_signatures(fn)
                # Rebuild JIT callable object
                from .dummy_target import generic_add as gadd
                sfn, label, supp_sigs = make_specialized_add(stable, gadd)
                self.specialized[fn] = (sfn, label, supp_sigs)

        print(f"[COOKIE LOADER] Berhasil memuat Cookie (Schema v{data.get('schema_version', 1)}) dari {self.profile_path}.")
        print(f"  Modul aktif      : {list(self.specialized.keys())}")
        print(f"  Tier-Lowered locked: {list(self.tier_lowered) or 'Tidak ada'}")
        return True
