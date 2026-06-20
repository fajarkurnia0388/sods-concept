# SODS — Matriks Status Peta Jalan (*Roadmap Status Matrix*)

> Diperbarui: 20 Juni 2026  
> Evaluator independen: Arena.ai

| Kapabilitas | Status | Catatan |
|---|---|---|
| Polymorphic Inline Caches (PIC) | ✅ Terimplementasi (*Implemented*) | Pembungkus (*wrapper*) Python, `type(a) in allowed_types` |
| OSR Deoptimization | ✅ Terimplementasi (*Implemented*) | Pencadangan (*fallback*) Python |
| Tier-Lowering Protection | ✅ Terimplementasi (*Implemented*) | Ambang batas (*threshold*) 30%, himpunan terkunci |
| Cookie Persistence | ✅ HMAC-SHA256 + chmod 400 | Peta Jalan (*Roadmap*): Ed25519 |
| WASI I/O Boundary | ⚠️ Disimulasikan (*Simulated*) | Bendera (*flag*) `is_io_side_effect` manual |
| PEP 669 sys.monitoring | ✅ Minimal | Peristiwa CALL terdaftar (Python 3.12+) |
| eBPF / DynamoRIO | ❌ Peta Jalan (*Roadmap*) | Fase 2 — belum ada kode |
| PMU Sampling | ❌ Peta Jalan (*Roadmap*) | Fase 1 |
| Timing Noise Randomization | ❌ Peta Jalan (*Roadmap*) | — |
| Tauri Companion Runtime | ❌ Rencana Selanjutnya (*Future Work*) | Fase 4 |

### Tolok Ukur (*Benchmark*) (CPython 3.13, Linux x86_64, 50k operasi)

| Skenario | SODS | Garis Dasar (*Baseline*) | Peningkatan Kecepatan (*Speedup*) |
|---|---|---|---|
| A Stabil (int+int) | ~10.0 ms | generic_add ~31.3 ms | **3.1–3.25×** |
| A vs bawaan (*native*) | ~10.0 ms | operator.add ~2.3 ms | **0.23–0.24× (4.26× lebih lambat)** |
| B Volatile (campuran) | ~56.0 ms | generic_add ~38 ms | **0.68–0.69× (31% lebih lambat)** |

**Keputusan (*Verdict*):** PoC JIT Edukatif — sangat baik untuk mengajarkan PIC/Guard/OSR/Tier-Lowering. Bukan untuk produksi (*production*). Untuk kecepatan nyata: Numba / PyPy / Cython. Untuk mengatasi kebengkakan Electron: Tauri.

Angka tolok ukur (*benchmark*) dapat direproduksi melalui:
```bash
PYTHONPATH=src python3 benchmarks/bench_add.py
```

Lihat detail teknis di [`WHITEPAPER.md`](./WHITEPAPER.md) Bab 5.3.
