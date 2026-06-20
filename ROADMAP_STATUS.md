# SODS — Roadmap Status Matrix

> Diperbarui: 20 Juni 2026  
> Evaluator independen: Arena.ai

| Kapabilitas | Status | Catatan |
|---|---|---|
| Polymorphic Inline Caches (PIC) | ✅ Implemented | Python wrapper, `type(a) in allowed_types` |
| OSR Deoptimization | ✅ Implemented | Python fallback |
| Tier-Lowering Protection | ✅ Implemented | 30% threshold, lock set |
| Cookie Persistence | ✅ HMAC-SHA256 + chmod 400 | Roadmap: Ed25519 |
| WASI I/O Boundary | ⚠️ Simulated | Manual `is_io_side_effect` flag |
| PEP 669 sys.monitoring | ✅ Minimal | CALL events registered (Python 3.12+) |
| eBPF / DynamoRIO | ❌ Roadmap | Fase 2 — belum ada kode |
| PMU Sampling | ❌ Roadmap | Fase 1 |
| Timing Noise Randomization | ❌ Roadmap | — |
| Tauri Companion Runtime | ❌ Future Work | Fase 4 |

### Benchmark (CPython 3.13, Linux x86_64, 50k ops)

| Skenario | SODS | Baseline | Speedup |
|---|---|---|---|
| A Stabil (int+int) | ~10.0 ms | generic_add ~31.3 ms | **3.1–3.25×** |
| A vs native | ~10.0 ms | operator.add ~2.3 ms | **0.23–0.24× (4.26× slower)** |
| B Volatile (mixed) | ~56.0 ms | generic_add ~38 ms | **0.68–0.69× (31% slower)** |

**Verdict:** Educational PoC JIT — excellent for teaching PIC/Guard/OSR/Tier-Lowering. Not production. For real speed: Numba / PyPy / Cython. For Electron bloat: Tauri.

See full evaluation: [`EVALUASI_SODS_ROUND2_20260620.md`](./EVALUASI_SODS_ROUND2_20260620.md)
