# 🎧 KyaNaDeApp

**KyaNaDeApp** adalah sebuah aplikasi desktop eksperimental berbasis Python yang memungkinkan pengguna untuk memutar lagu baik secara **offline** (dari folder lokal) maupun **online streaming** langsung dari **YouTube** tanpa iklan.

> Proyek ini dibuat sebagai latihan pribadi, showcase, dan eksperimen GUI, dan saat ini **sudah tidak dilanjutkan lagi (discontinued)**.

---

## ✨ Fitur Utama

- 🎵 **Mode Offline**:
  - Memutar file `.mp3` dari folder `songs/`
  - Menampilkan daftar lagu offline
  - Tombol play & stop sederhana

- 🌐 **Mode Online (YouTube)**:
  - Streaming lagu dari hasil pencarian YouTube
  - Mendukung URL langsung atau judul pencarian
  - Kontrol: Play, Pause/Resume, Stop

- 🔁 **Switch Mode**: Ganti antara offline dan online hanya dengan satu tombol.

- 📥 **Downloader terpisah**:
  - `DownloaderSimpleYtMp3.py` memungkinkan download video YouTube sebagai file MP3
  - Hasil disimpan ke folder `songs/` otomatis

---

## 🧠 Teknologi & Library

- Python 3.10+
- GUI: 
  - [KivyMD](https://github.com/kivymd/KivyMD)
  - [PySide6](https://doc.qt.io/qtforpython/)
- YouTube Handling: 
  - [`yt_dlp`](https://github.com/yt-dlp/yt-dlp)
- Audio Player:
  - [`ffpyplayer`](https://github.com/matham/ffpyplayer)

---

## 📁 Struktur Direktori

```
KyaNaDeApp/
├── data/                # Data settings & playlist
├── download/            # Downloader logic
├── player/              # Online & offline audio player
├── search/              # Pencarian YouTube & lokal
├── ui/                  # UI berbasis KivyMD (.kv)
├── main.py              # Entry point utama
├── requirements.txt     # Semua dependensi
├── README.md            # File ini
```

---

## ⚠️ Status Proyek

❌ **Proyek ini tidak lagi dikembangkan.**

KyaNaDeApp dibuat sebagai bagian dari eksperimen pribadi untuk belajar tentang:
- GUI ganda (KivyMD & PySide)
- Pemrosesan audio
- Streaming YouTube langsung tanpa download

Walau fiturnya berfungsi, **proyek ini sekarang sudah ditinggalkan** untuk fokus pada proyek yang lebih matang & relevan.

---

## 📸 Tampilan (Optional)

_Tambahkan screenshot jika ada, misalnya dari file PNG yang kamu kirim sebelumnya._

---

## ✅ Cara Menjalankan

```bash
pip install -r requirements.txt
python main.py
```

Untuk menjalankan downloader sederhana:
```bash
python DownloaderSimpleYtMp3.py
```

---

## 📩 Lisensi

Proyek ini bersifat open-source dan bebas digunakan untuk edukasi dan pengembangan pribadi.
