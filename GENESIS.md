# 🎬 Genesis Proyek: Narasi Filosofis "Ketika Performance Bukan Prioritas Lagi"

> Arsitektur **SODS (_Sandbox Observer-Driven Specializer_)** terlahir dari sebuah momen pencerahan mendadak setelah menyimak video esai fenomenal dari kanal YouTube **Di TeknoIn** berjudul [Ketika Performance Bukan Prioritas Lagi](https://www.youtube.com/watch?v=7zZSxjh72yk).  
> Dokumen ini menyajikan penulisan ulang narasi esai tersebut—mengurai benang merah dari keanggunan perangkat keras masa lalu, kehancuran ekosistem perangkat lunak modern, hingga terobosan rekayasa sistem yang memicu berdirinya repositori **`sods-runtime`**.

---

## 🚀 Bagian 1: Kontras Absolut (Apollo 11 vs Chrome 2026)

Bayangkan dua orang astronaut duduk di dalam kapsul roket Apollo 11, menembus luar angkasa sejauh 384.000 kilometer untuk mendaratkan kaki di bulan. Di balik misi paling legendaris dalam sejarah peradaban manusia tersebut, terdapat sebuah sistem navigasi roket (_Apollo Guidance Computer_) yang beroperasi hanya dengan **RAM 4 KB** dan ROM 72 KB.

Sebagai pembanding kontemporer: satu lembar foto _selfie_ berukuran 2 MB atau satu animasi _emote_ di WhatsApp memiliki jejak data setara 500 kali lipat dari seluruh kapasitas memori Apollo 11.

Di sisi lain, saat Anda menyalakan komputer hari ini, satu peramban Chrome dalam kondisi menunggu (_idle_) dengan mudah menelan **400 MB RAM**. Klien perpesanan seperti Discord atau Slack yang hanya berdiri diam di latar belakang sanggup merampas **500 MB hingga 1 GB RAM**. Kita hidup di era di mana RAM 8 GB mulai dipandang sebagai spesifikasi "minimum" untuk sekadar mengetik dokumen dan menjelajah web. Terdapat jurang keborosan yang melompat hingga **100.000 kali lipat** antara keanggunan komputasi 1969 berbanding realitas perangkat lunak hari ini. _Bagaimana peradaban pemrograman bisa sampai di titik ini?_

---

## 🏛️ Bagian 2: Warisan Dave Plummer dan Penolakan Abstraksi

Di era 1970-an hingga awal 1990-an, pengembang perangkat lunak tidak memiliki jalur pelarian selain **disiplin dan efisiensi mutlak**. Silikon dan RAM bernilai teramat mahal—bisa setara puluhan hingga ratusan juta rupiah per megabyte. Setiap _byte_ memori yang disia-siakan adalah pengkhianatan terhadap anggaran perusahaan atau negara.

Para programmer di masa itu menulis instruksi murni menggunakan bahasa _Assembly_ atau C tingkat rendah. Tidak ada _framework_ pembantu atau abstraksi mewah. Pengembang tahu secara pasti apa yang berdetak di dalam setiap siklus prosesor (_CPU cycle_). Hasilnya terbukti spektakuler: mahakarya John Carmack, _Doom_ (1993), sanggup menghadirkan pesona 3D interaktif di atas **RAM 4 MB** memanfaatkan inovasi algoritma _Binary Space Partitioning_ (BSP).

Namun, teladan arsitektur yang paling membumi adalah sebuah tool yang hampir semua pengguna Windows pernah sentuh: **Task Manager**.
Pada pertengahan 1990-an, Dave Plummer (seorang insinyur veteran Microsoft) membangun Windows Task Manager di waktu luangnya. Karena tugas utama aplikasi ini adalah menolong sistem operasi yang sedang mengalami kelumpuhan (_crash_), Task Manager diharamkan untuk ikut-ikutan _crash_. Plummer menulis kodenya secara ketat dalam bahasa C, menekan konsumsi memori murni hingga menyusut ke **80 KB RAM**, memastikan aplikasi kelak selalu sanggup dipanggil bahkan saat memori OS telah terfragmentasi parah.

Lebih mengagumkan lagi adalah cara Plummer memecahkan persoalan konkurensi: _bagaimana memastikan Task Manager tidak terbuka dua instansi sekaligus saat pengguna panik menekan tombol berkali-kali?_
Solusinya teramat anggun. Saat Task Manager diluncurkan, ia menanamkan sebuah **penanda unik (_memory marker mutex_)** di dalam RAM. Apabila penanda tersebut telah terdeteksi, berarti instansi Task Manager lain sudah berjalan. Bukannya memuat jendela baru yang membebani OS, ia cukup menyuruh jendela yang sudah ada untuk melompat ke depan (_bring to front_), lalu instansi kedua tersebut langsung bunuh diri secara membanggakan. _Di masa lalu, setiap keputusan desain berpusat pada empati terhadap keterbatasan hardware._

---

## ⚡ Bagian 3: Kehancuran Natural (Wirth's Law & Paradoks Jevons)

Ketika Hukum Moore perlahan menurunkan harga SSD dan silikon hingga melimpah dan luar biasa murah, dinamika psikologis dunia pemrograman pun berubah total. Tekanan untuk berhemat menghilang secara natural. Muncul bahasa tingkat tinggi berlapis, _package manager_ yang mengimpor ribuan pustaka (_dependencies_), serta dogma abstraksi demi memanjakan produktivitas insinyur.

Di sinilah **Penyakit Ekosistem Modern** mulai tumbuh subur:

1. **Hukum Wirth (_Wirth's Law_):** _Perangkat lunak melambat jauh lebih cepat daripada peningkatan kecepatan hardware_. Sebagian besar keuntungan yang diberikan oleh prosesor tercepat hari ini habis terbakar semata-mata untuk menutupi tumpukan _overhead_ dari kerangka kerja tingkat tinggi.
2. **Kutukan Framework Electron:** Idenya terdengar luar biasa mulia—_"Tulis kode web (HTML/CSS/JS) sekali, lalu jalankan sebagai aplikasi desktop di semua OS"_. Namun implementasinya luar biasa brutal. Framework Electron menempelkan satu salinan utuh peramban Chromium dan _engine runtime_ Node.js di dalam setiap aplikasi. Akibatnya, saat Anda membuka VS Code, Slack, Spotify, dan Discord serentak, laptop Anda terpaksa memuat empat peladen Chromium terpisah ke dalam RAM.
3. **Paradoks Jevons (_Jevons Paradox_):** _Ketika sumber daya hardware menjadi lebih murah dan efisien, manusia tidak menggunakannya lebih sedikit, melainkan meledak menggunakannya lebih boros_. Storage murah memicu penumpukan log tak terkelola; _bandwidth_ cepat membuat peramban menyedot puluhan iklan, pelacak (_trackers_), dan _video autoplay_ di latar belakang sebelum baris pertama artikel muncul di layar.

**Mengapa korporasi raksasa tidak mau memperbaikinya?** Jawabannya adalah realitas bisnis yang murni dan dingin: **Karena tidak menguntungkan**.
Mempekerjakan satu _Senior Systems Engineer_ selama berbulan-bulan hanya untuk memangkas _overhead_ 300 MB RAM akan membakar anggaran ratusan juta rupiah per bulan. Bagi korporasi, jauh lebih murah membiarkan aplikasi mereka bengkak, merilis fitur baru secepat mungkin ke pasar, dan memaksa pengguna yang menanggung bebannya dengan cara meng- _upgrade_ RAM spesifikasi laptop mereka. _Fokus industri telah berganti dari keanggunan komputasi menjadi kecepatan bisnis._

---

## 💡 Bagian 4: Lompatan Deduktif Fajar Kurnia (Lahirnya SODS)

Selesai merenungkan esai mendalam dari _Di TeknoIn_ tersebut, **Fajar Kurnia** menolak untuk sekadar meratapi nasib atau berfantasi menuntut korporasi global menulis ulang (_rewrite_) jutaan baris kode aplikasi Electron mereka ke dalam bahasa Rust atau C.

Fajar mengambil satu lompatan deduktif yang brilian, memadukan ilmu kompilator dengan realitas industri, dan merumuskan cetak biru repositori **`sods-runtime`**:

```
[Realitas Pasar: Esai Di TeknoIn]
"Korporasi tidak akan merilis biner efisien karena mahal & melambatkan bisnis."
                              │
                              ▼
[Batas Komputasi Formal: Teorema Rice]
"Kita tidak bisa membuat konverter biner statis universal yang dijamin ekuivalen."
                              │
                              ▼
[Terobosan Fajar Kurnia: Arsitektur SODS Produksi]
"KITA BANGUN SAJA RUNTIME WRAPPER TINGKAT SISTEM OPERASI SECARA EKSTERNAL!"
"Telan biner Electron yang bengkak apa adanya di disk (Zero-Modification)."
"Host Sandbox kita yang akan mengamati eksekusi secara otonom (Cold Run)."
"Begitu pola teramati, POTONG OVERHEAD DISPATCH DINAMIS via PIC JIT Emitter."
"Jaga kebenaran 100% via pengawalan Guards dan evakuasi OSR (Deoptimization)."
```

Melalui SODS, Fajar memodelkan sebuah tool perantara yang **mendistribusikan keanggunan JIT Compiler murni kepada aplikasi-aplikasi yang tidak memilikinya**. Kita tidak perlu merubah cara pengembang menulis kode; mesin _Hypervisor OS_ kitalah yang akan menyihir komputasi mereka di perbatasan eksekusi (_Runtime Specialization_).

---

## 🌟 Penutup: Manifesto Pencerahan Perangkat Keras

Game _Sifu_ (2022) sanggup menghadirkan dunia aksi 3D yang begitu menakjubkan hanya di dalam ukuran **1.2 GB**, berjalan lancar di hardware berusia 10 tahun. Sementara game AAA lain menuntut _storage_ 150 GB and masih sering mengalami _stuttering_.

Hal ini membuktikan satu kebenaran mutlak: **Efisiensi bukanlah keahlian yang hilang dari dunia rekayasa komputasi, melainkan insentifnya yang telah terlupakan**. Melalui arsitektur SODS, kita mengembalikan insentif keanggunan tersebut, membuktikan bahwa perangkat lunak modern tetap sanggup berjalan seramping dan sekencang perangkat keras mentah era Apollo 11.

Terima kasih, **Di TeknoIn**, atas karya yang telah menggetarkan nalar dan memicu berdirinya rancang bangun mahakarya riset ini!
