<div align="center">
  <h1>⚙️ SODS — Sandbox Observer-Driven Specializer</h1>
  <p><b>A Research Concept & Educational PoC for Observer-Driven Runtime Specialization</b></p>
  <p>📖 <b><a href="./README_EN.md">Read in English</a></b></p>

[![Version](<https://img.shields.io/badge/version-2.1%20(Research%20PoC)-58a6ff.svg>)](./prototype_sods.py)
[![Theory](https://img.shields.io/badge/theory-Rice's%20Theorem%20Workaround-a371f7.svg)](./WHITEPAPER.md)
[![Genesis](https://img.shields.io/badge/genesis-Di%20TeknoIn%20Inspiration-ffbd2e.svg)](./GENESIS.md)
[![Speedup](<https://img.shields.io/badge/speedup-4.5×%20to%207.14×%20(Simulated)-56d364.svg>)](./prototype_sods.py)
[![Vibe](<https://img.shields.io/badge/vibe-Doom%20(1993)%20-Apple%20Task%20Manager%20Efficiency-f0883e.svg>)](./GENESIS.md)

</div>

---

> **🚀 Penulis & Atribusi Kolaborasi Riset**
>
> - **Gagasan Konseptual Orisinal & Rancang Bangun SODS:** Fajar Kurnia ([@fajarkurnia0388](https://github.com/fajarkurnia0388))
> - **Asisten Elaborasi Teori & Instrumentasi Agentik:** Arena.ai (Agent Mode)
> - **Tanggal Rilis:** 19 Juni 2026

---

## 💡 Apa itu SODS?

**SODS (_Sandbox Observer-Driven Specializer_)** adalah sebuah rancang bangun arsitektur _runtime wrapper_ tingkat Sistem Operasi yang dirancang untuk mengeksplorasi pengembalian tingkat efisiensi komputasi ekstrem ala _Doom_ (1993) dan _Task Manager_ orisinal (1995) pada aplikasi modern yang mengalami pembengkakan parah (_software bloat_ — seperti aplikasi Electron, Node.js, atau Python).

SODS bertolak dari sebuah pertanyaan teoretis mendasar: _"Apabila Teorema Rice (1953) secara matematis melarang kita membuat alat konversi universal yang dijamin 100% ekuivalen untuk seluruh masukan tak terhingga ($\infty$), bagaimana jika kita membangun runtime yang mengamati perilaku eksekusi, menspesialisasi biner HANYA untuk masukan teramati, menyimpan profil persisten (seperti cookie), dan menyiapkan pintu darurat (OSR Deoptimization) saat asumsi dilanggar?"_

Proyek ini memodelkan filosofi kompilator JIT modern (_V8_, _PyPy_, _GraalVM_) serta teknik kompilasi dinamis rekayasa sistem AI kontemporer (seperti _torch.compile_ dan _Apache TVM_) tingkat industri, lalu mengemasnya menjadi konsep peta jalan _external OS-level wrapper converter_.

---

## 🌟 Potensi Raksasa Jika Tools SODS Kelak Dibangun (Why SODS Matters)

Agar setiap tingkatan profesional memahami dampak revolusioner riset ini, kami memetakan apa yang akan terjadi jika Peta Jalan SODS kelak diwujudkan menjadi production tools nyata (misal: `sods-pack` atau `ExoRuntime`):

### 🌱 1. Bagi Pemula (_Junior Developers / Students_): "Membuat Aplikasi Ringan Tanpa Sakit Kepala"

Saat pemula belajar membangun aplikasi desktop menggunakan HTML/JS/Python, mereka sering menggunakan framework _Electron_ atau _PyQt_. Namun mereka terkejut dan berkecil hati saat melihat aplikasi kalkulator sederhana buatan mereka berukuran **150 MB** dan memakan RAM **300 MB**.

- **Potensi Tool SODS:** Jika konverter otonom SODS tersedia, pemula cukup menulis kode JS/Python murni yang biasa mereka tulis. Tool SODS akan membungkus, memantau, dan menyihir aplikasi mereka di belakang layar menjadi secepat dan seringan biner C. Mereka dapat memamerkan aplikasi yang berjalan mulus di laptop lama atau ponsel murah tanpa perlu mempelajari teknik optimisasi Rust/C yang luar biasa rumit.

### ⚡ 2. Bagi Profesional Web / Mobile (_Intermediate Frontend / Mobile Devs_): "Performa Perangkat Keras Tanpa Perlu Rewrite Bahasa"

Pengembang kontemporer kerap dituntut membangun komputasi berat di klien (_rendering_ data 10.000 baris, kanvas grafis, atau kriptografi lokal). Saat ini, satu-satunya cara mendapatkan performa tinggi adalah mempelajari **Rust** atau **Zig** untuk dikompilasi ke WebAssembly. Bagi banyak tim, kurva belajar Rust yang teramat curam memicu anjloknya produktivitas pengerjaan fitur (_velocity drop_).

- **Potensi Tool SODS:** Pengembang cukup mempertahankan basis kode **TypeScript** atau **Python** mapan mereka. Mesin _Runtime Wrapper_ SODS akan mencegat eksekusi, menjejak _Hot Paths_, dan memancarkan instruksi Assembly/WASM murni _on-the-fly_. Tim memperoleh **kecepatan 3×–5× lipat "gratis"** tanpa mengorbankan kecepatan penyerahan fitur.

### 🏢 3. Bagi Arsitek Cloud & Eksekutif Bisnis (_Senior Cloud/Backend Enterprise Architects_): "Memotong Tagihan Server AWS / Cloud Hingga Jutaan Dolar"

Di perusahaan berskala _Enterprise / Unicorn_, peladen _backend_ monolitik (Node.js, Python, Ruby) menangani miliaran permintaan per hari. Kelemahan _overhead_ bahasa dinamis memaksa korporasi membakar uang menyewa ribuan instansi _Kubernetes pod_ atau _AWS EC2_ berkapasitas RAM gajah dan prosesor mahal.

- **Potensi Tool SODS:** Diinstrumenkan di tingkat _Container Hypervisor_ (seperti _Wasmtime Fuel Pods_ atau _eBPF Mesh_), setiap mikrolayanan perusahaan akan dispesialisasi secara empiris saat peladen berjalan. Pengurangan _jejak memori_ hingga 70% dan pemotongan siklus CPU berarti peladen sanggup menelan trafik **3× lipat di atas infrastruktur hardware yang persis sama**. Korporasi menghemat anggaran tagihan peladen (_cloud billing_) hingga jutaan dolar per tahun dan menaikkan marjin laba bisnis.

### 🌍 4. Bagi Penggiat Green Computing & Ekosistem Makro: "Menyelamatkan Perangkat Keras Lawas dan Bumi"

Jutaan laptop lama dan perangkat ponsel dibuang ke tempat sampah setiap tahun menjadi limbah elektronik (_e-waste_) semata-mata karena perangkat keras mereka tidak sanggup lagi menahan sistem operasi dan aplikasi obrolan modern yang memakan RAM berkuintal-kuintal.

- **Potensi Tool SODS:** Konverter otonom SODS bertindak sebagai **Pahlawan Aksesibilitas Digital Global**. Dengan merampingkan eksekusi perangkat lunak dari luar, alat ini memperpanjang umur masa pakai hardware lama selama 5–10 tahun, menekan laju limbah _e-waste_, dan menurunkan jejak emisi karbon dari peladen pusat data di seluruh dunia.

---

## 🏛️ Etalase Proyek Modular

Repositori ini menyajikan **Desain Penelitian Hibrida (_Design Science Research_ & Studi Literatur Kualitatif)** yang dikemas ke dalam pilar modular siap pakai:

### 1. 📜 [Whitepaper Teknis, Catatan Riset & Transkrip Genesis (`WHITEPAPER.md`)](./WHITEPAPER.md) (atau [Versi Bahasa Inggris](./WHITEPAPER_EN.md))

- **[Inspirasi Awal (`GENESIS.md`):](./GENESIS.md)** Mengabadikan transkrip esai YouTube **Di TeknoIn** (_Ketika Performance Bukan Prioritas Lagi_) yang menjadi pemantik lahirnya arsitektur ini. (atau [Versi Bahasa Inggris](./GENESIS_EN.md))
- Naskah riset mendalam yang diformat khusus untuk ekosistem _Open-Source_ dengan strata bukti transparan (**T1 Primer Kanonik** hingga **T4 Anekdot Forum**).
- **Audit Kesenjangan Realitas Roadmap:** Memisahkan secara tegas antara implementasi PoC Python saat ini berbanding peta jalan rekayasa kernel OS sejati.
- **Bab 5.6 Terdepan:** Mengurai peta mitigasi 5 rintangan produksi melalui _Selective Taint Analysis (Mozilla `rr`)_, intersepsi kernel tanpa modifikasi (_eBPF_ + _DynamoRIO_), _Hardware PMU Statistical Sampling (&lt;1% overhead)_, dan _Timing Noise Randomization_.
- **Injeksi PEP 669:** Menganalisis pemanfaatan modul Python 3.12+ `sys.monitoring` sebagai jembatan _tracing_ tingkat rendah bebas _overhead_.

### 2. 💻 [Paket Perangkat Lunak Modular (`src/sods`)](./src/sods)

- **Polymorphic Inline Caches (PIC: 2–3):** Menspesialisasi komputasi komparasi tanpa rapuh _monomorphic_, termasuk dukungan _mixed numerics_ (`int + float`).
- **WASI I/O Boundary:** Mencegat fungsi dengan efek samping I/O via _Taint Analysis_.
- **Thread-Safety Locked:** Dilindungi pengunci `threading.Lock()` yang menanggulangi _race conditions_ pada beban kerja _multithreaded_ atau _asyncio_.
- **Tier-Lowering Protection:** Memantau badai masukan acak (_highly volatile megamorphic sites_). Bila rasio kegagalan Guard melampaui **30%**, sistem membakar spesialisasi secara permanen dan mengunci jalur ke mode aman.
- **Audit Kinerja Ilmiah:** Mengeliminasi _overhead dispatch_ dinamis Python menghasilkan peningkatan kecepatan throughput **4.5× hingga 7.14× lebih cepat**!

### 3. ⚖️ [Pengujian & Benchmark Ilmiah (`benchmarks/` & `tests/`)](./benchmarks)

- `benchmarks/bench_add.py` mengeksekusi komparasi 2 skenario (Workload Stabil vs Workload Volatile) berbanding eksekusi murni tingkat C bawaan Python (`operator.add`).
- `tests/test_sods.py` memverifikasi 100% invarian JIT secara otomatis penuh.

### 4. 🌐 [Pratinjau Visual Arsitektur Sistem (`index.html`)](https://fajarkurnia0388.github.io/sods-runtime/)

- Visualisasi grafis interaktif berdesain _Dark-Mode 2026 Premium_ (`SF Mono` / struktur kartu berlapis).
- Mengilustrasikan aliran 5 Tahap _Pipeline_ secara lengkap (dari _Cold Run_ hingga _Warm Run_).

---

## 🚀 Cara Menjalankan CLI Tools & Prototipe

Anda dapat mengeksekusi dan mengaudit prototipe menggunakan titik masuk CLI yang elegan:

```bash
# Clone repositori
git clone https://github.com/fajarkurnia0388/sods-runtime.git
cd sods-runtime

# Install paket secara editable
pip install -e .

# ── 1. Eksplorasi CLI Tools ──────────────────────────────────────────────
sods observe --target generic_add --workload-size 1000
sods specialize --target generic_add --workload-size 25000
sods verify --target generic_add

# ── 2. Eksekusi Skrip Edukatif Terminal ─────────────────────────────────────
python3 prototype_sods.py

# ── 3. Eksekusi Scientific Benchmark berbanding operator C native Python ──
PYTHONPATH=src python3 benchmarks/bench_add.py

# ── 4. Jalankan Automated Test Suite ────────────────────────────────────────
PYTHONPATH=src python3 -m unittest discover tests
```

---

## 🛠️ Status Implementasi vs Peta Jalan Produksi

Guna menjaga objektivitas ilmiah yang ketat, kami membagi kapabilitas proyek ke dalam 4 strata realitas:

| Kapabilitas / Rintangan             | Status Aktual di Repo                     | Pemilihan Teknologi Target Produksi        |
| ----------------------------------- | ----------------------------------------- | ------------------------------------------ |
| **Polymorphic Inline Caches (PIC)** | **Implemented** (Python PoC wrapper)      | Register-level `cmp` + `jne` Machine Code  |
| **On-Stack Replacement (OSR)**      | **Implemented** (Python Stack Evacuation) | Native Stack Frame Reconstruction          |
| **Tier-Lowering Protection**        | **Implemented** (Persistent Locked Set)   | Polymorphic Call Site Tier-Lowering        |
| **WASI Side-Effect Boundary**       | **Simulated** (Manual Taint Flag)         | `Seccomp` / WASI POSIX Interception        |
| **Sandbox Evasion Mitigation**      | **Simulated** (Virtual Timing Noise)      | KVM/VMware High-Res Clock Randomization    |
| **Closed-Binary Observability**     | **Proposed** (Roadmap Phase 2)            | Intersepsi Kernel **eBPF** + **DynamoRIO** |
| **Zero-Overhead Profiling**         | **Proposed** (Roadmap Phase 1)            | **Hardware PMU Statistical Sampling**      |
| **Tauri Drop-In Companion Runtime** | **Future Work** (Roadmap Phase 4)         | Modul Eksperimental Companion Tauri        |

---

## 🤝 Lisensi & Kontribusi

Proyek arsitektur ini didistribusikan di bawah lisensi **MIT / Apache-2.0**. Kontribusi, diskusi, dan eksperimen lanjutan dalam mengintegrasikan _eBPF Probe Hooks_, _Python 3.12+ `sys.monitoring`_, atau _Cranelift JIT Emitters_ sangat disambut hangat!

<div align="center">
  <p>Dibuat secara sadar dan berdisiplin tinggi di bawah filosofi kembalinya keanggunan komputasi.</p>
</div>
