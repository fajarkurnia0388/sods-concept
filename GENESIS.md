# 🎬 Genesis Proyek: Narasi Filosofis "Ketika Performance Bukan Prioritas Lagi"

> Arsitektur **SODS (*Sandbox Observer-Driven Specializer*)** terlahir dari sebuah momen pencerahan mendadak setelah menyimak video esai fenomenal dari kanal YouTube **Cemw Anyway** berjudul [Ketika Performance Bukan Prioritas Lagi](https://www.youtube.com/watch?v=7zZSxjh72yk).  
> Dokumen ini menyajikan penulisan ulang narasi esai tersebut—mengurai benang merah dari keanggunan silikon masa lalu, kehancuran ekosistem perangkat lunak modern, hingga terobosan rekayasa sistem yang memicu berdirinya repositori **`sods-runtime`**.

---

## 🚀 Bagian 1: Kontras Absolut (Apollo 11 vs Chrome 2026)

Bayangkan dua orang astronaut duduk di dalam kapsul roket Apollo 11, menembus luar angkasa sejauh 384.000 kilometer untuk mendaratkan kaki di bulan. Di balik misi paling legendaris dalam sejarah peradaban manusia tersebut, terdapat sebuah sistem navigasi roket (*Apollo Guidance Computer*) yang beroperasi hanya dengan **RAM 4 KB** dan ROM 72 KB.

Sebagai pembanding kontemporer: satu lembar foto *selfie* berukuran 2 MB atau satu animasi *emote* di WhatsApp memiliki jejak data setara 500 kali lipat dari seluruh kapasitas memori Apollo 11. 

Di sisi lain, saat Anda menyalakan komputer hari ini, satu peramban Chrome dalam kondisi menunggu (*idle*) dengan mudah menelan **400 MB RAM**. Klien perpesanan seperti Discord atau Slack yang hanya berdiri diam di latar belakang sanggup merampas **500 MB hingga 1 GB RAM**. Kita hidup di era di mana RAM 8 GB mulai dipandang sebagai spesifikasi "minimum" untuk sekadar mengetik dokumen dan menjelajah web. Terdapat jurang keborosan yang melompat hingga **100.000 kali lipat** antara keanggunan komputasi 1969 berbanding realitas perangkat lunak hari ini. *Bagaimana peradaban pemrograman bisa sampai di titik ini?*

---

## 🏛️ Bagian 2: Warisan Dave Plummer dan Penolakan Abstraksi

Di era 1970-an hingga awal 1990-an, pengembang perangkat lunak tidak memiliki jalur pelarian selain **disiplin dan efisiensi mutlak**. Silikon dan RAM bernilai teramat mahal—bisa setara puluhan hingga ratusan juta rupiah per megabyte. Setiap *byte* memori yang disia-siakan adalah pengkhianatan terhadap anggaran perusahaan atau negara.

Para programmer di masa itu menulis instruksi murni menggunakan bahasa *Assembly* atau C tingkat rendah. Tidak ada *framework* pembantu atau abstraksi mewah. Pengembang tahu secara pasti apa yang berdetak di dalam setiap siklus prosesor (*CPU cycle*). Hasilnya terbukti spektakuler: mahakarya John Carmack, *Doom* (1993), sanggup menghadirkan pesona 3D interaktif di atas **RAM 4 MB** memanfaatkan inovasi algoritma *Binary Space Partitioning* (BSP).

Namun, teladan arsitektur yang paling membumi adalah sebuah perkakas yang hampir semua pengguna Windows pernah sentuh: **Task Manager**.
Pada pertengahan 1990-an, Dave Plummer (seorang insinyur veteran Microsoft) membangun Windows Task Manager di waktu luangnya. Karena tugas utama aplikasi ini adalah menolong sistem operasi yang sedang mengalami kelumpuhan (*crash*), Task Manager diharamkan untuk ikut-ikutan *crash*. Plummer menulis kodenya secara ketat dalam bahasa C, menekan konsumsi memori murni hingga menyusut ke **80 KB RAM**, memastikan aplikasi kelak selalu sanggup dipanggil bahkan saat memori OS telah terfragmentasi parah.

Lebih mengagumkan lagi adalah cara Plummer memecahkan persoalan konkurensi: *bagaimana memastikan Task Manager tidak terbuka dua instansi sekaligus saat pengguna panik menekan tombol berkali-kali?*
Solusinya teramat anggun. Saat Task Manager diluncurkan, ia menanamkan sebuah **penanda unik (*memory marker mutex*)** di dalam RAM. Apabila penanda tersebut telah terdeteksi, berarti instansi Task Manager lain sudah berlari. Bukannya memuat jendela baru yang membebani OS, ia cukup menyuruh jendela yang sudah ada untuk melompat ke depan (*bring to front*), lalu instansi kedua tersebut langsung bunuh diri secara membanggakan. *Di masa lalu, setiap keputusan desain berpusat pada empati terhadap keterbatasan perangkat keras.*

---

## ⚡ Bagian 3: Kehancuran Natural (Wirth's Law & Paradoks Jevons)

Ketika Hukum Moore perlahan menurunkan harga SSD dan silikon hingga melimpah dan luar biasa murah, dinamika psikologis dunia pemrograman pun berubah total. Tekanan untuk berhemat menghilang secara natural. Muncul bahasa tingkat tinggi berlapis, *package manager* yang mengimpor ribuan pustaka (*dependencies*), serta dogma abstraksi demi memanjakan produktivitas insinyur.

Di sinilah **Penyakit Ekosistem Modern** mulai tumbuh subur:
1. **Hukum Wirth (*Wirth's Law*):** *Perangkat lunak melambat jauh lebih cepat daripada peningkatan kecepatan perangkat keras*. Sebagian besar keuntungan yang diberikan oleh prosesor tercepat hari ini habis terbakar semata-mata untuk menutupi tumpukan *overhead* dari kerangka kerja tingkat tinggi.
2. **Kutukan Framework Electron:** Idenya terdengar luar biasa mulia—*"Tulis kode web (HTML/CSS/JS) sekali, lalu jalankan sebagai aplikasi desktop di semua OS"*. Namun implementasinya luar biasa brutal. Framework Electron menempelkan satu salinan utuh peramban Chromium dan *engine runtime* Node.js di dalam setiap aplikasi. Akibatnya, saat Anda membuka VS Code, Slack, Spotify, dan Discord serentak, laptop Anda terpaksa memuat empat peladen Chromium terpisah ke dalam RAM.
3. **Paradoks Jevons (*Jevons Paradox*):** *Ketika sumber daya keras menjadi lebih murah dan efisien, manusia tidak menggunakannya lebih sedikit, melainkan meledak menggunakannya lebih boros*. Storage murah memicu penumpukan log tak terkelola; *bandwidth* cepat membuat peramban menyedot puluhan iklan, pelacak (*trackers*), dan *video autoplay* di latar belakang sebelum baris pertama artikel muncul di layar.

**Mengapa korporasi raksasa tidak mau memperbaikinya?** Jawabannya adalah realitas bisnis yang murni dan dingin: **Karena tidak menguntungkan**.
Mempekerjakan satu *Senior Systems Engineer* selama berbulan-bulan hanya untuk memangkas *overhead* 300 MB RAM akan membakar anggaran ratusan juta rupiah per bulan. Bagi korporasi, jauh lebih murah membiarkan aplikasi mereka bengkak, merilis fitur baru secepat mungkin ke pasar, dan memaksa pengguna yang menanggung bebannya dengan cara meng- *upgrade* RAM spesifikasi laptop mereka. *Fokus industri telah berganti dari keanggunan komputasi menjadi kecepatan bisnis.*

---

## 💡 Bagian 4: Lompatan Deduktif Fajar Kurnia (Lahirnya SODS)

Selesai merenungkan esai mendalam dari *Cemw Anyway* tersebut, **Fajar Kurnia** menolak untuk sekadar meratapi nasib atau berfantasi menuntut korporasi global menulis ulang (*rewrite*) jutaan baris kode aplikasi Electron mereka ke dalam bahasa Rust atau C.

Fajar mengambil satu lompatan deduktif yang brilian, memadukan ilmu kompilator dengan realitas industri, dan merumuskan cetak biru repositori **`sods-runtime`**:

```
[Realitas Pasar: Esai Cemw Anyway]
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

Melalui SODS, Fajar memodelkan sebuah perkakas perantara yang **mendistribusikan keanggunan JIT Compiler murni kepada aplikasi-aplikasi yang tidak memilikinya**. Kita tidak perlu merubah cara pengembang menulis kode; mesin *Hypervisor OS* kitalah yang akan menyihir komputasi mereka di perbatasan eksekusi (*Runtime Specialization*).

---

## 🌟 Penutup: Manifesto Pencerahan Silikon
Game *Sifu* (2022) sanggup menghadirkan dunia aksi 3D yang begitu menakjubkan hanya di dalam ukuran **1.2 GB**, berlari lancar di keras berusia 10 tahun. Sementara game AAA lain menuntut *storage* 150 GB dan masih sering mengalami *stuttering*. 

Hal ini membuktikan satu kebenaran mutlak: **Efisiensi bukanlah keahlian yang hilang dari dunia rekayasa komputasi, melainkan insentifnya yang telah terlupakan**. Melalui arsitektur SODS, kita mengembalikan insentif keanggunan tersebut, membuktikan bahwa perangkat lunak modern tetap sanggup berlari seramping dan sekencang silikon mentah era Apollo 11.

Terima kasih, **Cemw Anyway**, atas karya yang telah menggetarkan nalar dan memicu berdirinya rancang bangun mahakarya riset ini!