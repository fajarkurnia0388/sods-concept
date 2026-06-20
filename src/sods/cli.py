"""
SODS Command-Line Interface (CLI)
=================================
Provides a terminal entrypoint for running Observer-Driven Specialization
workflows.
"""

import argparse
import sys
import os

from sods import SODSSandbox, EquivalenceVerifier
from sods.dummy_target import generic_add, generic_log_io

if sys.stdout and hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8')

def main():
    if len(sys.argv) == 2 and sys.argv[1] in ('-h', '--help'):
        parser = argparse.ArgumentParser(
            description="⚙️ SODS CLI — Educational PoC for Observer-Driven Runtime Specialization",
            formatter_class=argparse.RawTextHelpFormatter
        )
        subparsers = parser.add_subparsers(dest="command", help="Available execution workflows")
        subparsers.add_parser("observe", help="Run application workload in Cold Run mode to record PIC call profiles")
        subparsers.add_parser("specialize", help="Reconstitute profile JSON and execute warm run fast paths")
        subparsers.add_parser("verify", help="Run empirical equivalence verifier on bounded target domain inputs")
        subparsers.add_parser("bench", help="Run rigorous scientific benchmarks (Skenario A & B)")
        parser.parse_args(['--help'])
        return

    parser = argparse.ArgumentParser(
        description="⚙️ SODS CLI — Educational PoC for Observer-Driven Runtime Specialization",
        formatter_class=argparse.RawTextHelpFormatter
    )
    
    subparsers = parser.add_subparsers(dest="command", help="Available execution workflows", required=True)

    # ── Command 1: Observe ───────────────────────────────────────────────────
    parser_observe = subparsers.add_parser("observe", help="Run application workload in Cold Run mode to record PIC call profiles")
    parser_observe.add_argument("--target", type=str, default="generic_add", help="Target function name to observe (default: generic_add)")
    parser_observe.add_argument("--workload-size", type=int, default=1000, help="Number of profiling operations to observe (default: 1000)")
    parser_observe.add_argument("--taint-io", action="store_true", help="Simulate WASI boundary Side-Effect taint checking")

    # ── Command 2: Specialize ────────────────────────────────────────────────
    parser_spec = subparsers.add_parser("specialize", help="Reconstitute profile JSON and execute warm run fast paths")
    parser_spec.add_argument("--target", type=str, default="generic_add", help="Target function name to load fast path (default: generic_add)")
    parser_spec.add_argument("--workload-size", type=int, default=10000, help="Number of operations to run (default: 10000)")

    # ── Command 3: Verify ────────────────────────────────────────────────────
    parser_verify = subparsers.add_parser("verify", help="Run empirical equivalence verifier on bounded target domain inputs")
    parser_verify.add_argument("--target", type=str, default="generic_add", help="Target function name to verify (default: generic_add)")

    # ── Command 4: Bench ─────────────────────────────────────────────────────
    parser_bench = subparsers.add_parser("bench", help="Run rigorous scientific benchmarks (Skenario A & B)")

    args = parser.parse_args()

    # Instantiate central sandbox wrapper
    sandbox = SODSSandbox()

    if args.command == "bench":
        try:
            from benchmarks.bench_add import run_benchmarks
            run_benchmarks()
        except ImportError:
            print(" [ERROR] benchmarks module not found. Make sure you run from the project root or PYTHONPATH is set.")
            sys.exit(1)
        return

    if args.command == "observe":
        print("=" * 72)
        print(" 🔍 SODS CLI: COLD RUN PROFILE OBSERVATION".center(72))
        print("=" * 72)
        fn = generic_log_io if args.taint_io else generic_add
        
        workloads = [(i, i + 1) for i in range(args.workload_size)]
        if args.taint_io:
            workloads = [("Logging user transaction",)] * args.workload_size
            
        sandbox.cold_run(args.target, fn, workloads, is_io_side_effect=args.taint_io)
        sandbox.save_cookie()

    elif args.command == "specialize":
        print("=" * 72)
        print(" ⚡ SODS CLI: WARM RUN SPECIALIZATION EXECUTION".center(72))
        print("=" * 72)
        loaded = sandbox.load_cookie()
        if not loaded:
            print(" [ERROR] No persistence Cookie cache found! Please run 'sods observe' first.")
            sys.exit(1)
            
        workloads = [(i, i + 1) for i in range(args.workload_size)]
        results, deopts = sandbox.warm_run(args.target, generic_add, workloads)
        print(f"\n [DONE] {args.workload_size:,} operations completed.")
        print(f" • Sample Output  : {results[:3]}...")
        print(f" • OSR Evacuations: {deopts}x failures -> transparent fallback triggered.")

    elif args.command == "verify":
        print("=" * 72)
        print(" ⚖️ SODS CLI: EMPIRICAL EQUIVALENCE VERIFICATION".center(72))
        print("=" * 72)
        # Perform temporary cold run to build pure fast path
        workloads = [(i, i + 1) for i in range(100)]
        sandbox.cold_run(args.target, generic_add, workloads)
        if args.target in sandbox.specialized:
            sfn, label, _ = sandbox.specialized[args.target]
            EquivalenceVerifier.verify(args.target, generic_add, sfn, [(10, 20), (3.5, 4.5), (99, 1)])
        else:
            print(f" [ERROR] Specialized target '{args.target}' build not found.")

if __name__ == "__main__":
    main()
