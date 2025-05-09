# Sistem Manajemen Perpustakaan

## Anggota Tim
| No |     NIM    |        Nama        |
|----|------------|--------------------|
| 1  | 2211082012  |M. Zidhan Prasetyo  |
| 2  | 2211083011  |Exel Pratama        |    
| 3  | 2211081026  |Rifko Ahmad         |   
| 4  | 2122082026  |M. Arrazi Agazali    |  

## Deskripsi Proyek
Sistem Manajemen Perpustakaan adalah aplikasi web yang dibangun menggunakan Flask untuk mengelola data buku perpustakaan. Aplikasi ini mengintegrasikan MySQL untuk penyimpanan data dan Elasticsearch untuk fitur pencarian yang canggih. Sistem ini memungkinkan pengguna untuk menambah buku baru dan melakukan pencarian buku dengan cepat dan efisien.

## Fitur
- Manajemen data buku (tambah dan lihat)
- Pencarian buku menggunakan Elasticsearch
- Penyimpanan data di MySQL
- API RESTful untuk integrasi
- Antarmuka web yang responsif

## Persyaratan
- Python 3.x
- MySQL Server
- Elasticsearch 7.x
- Git

## Instalasi

1. Clone repository
bash
git clone [url-repository]
cd sistem-manajemen-perpustakaan


2. Buat dan aktifkan virtual environment
bash
python -m venv venv
# Untuk Windows
venv\Scripts\activate
# Untuk Linux/Mac
source venv/bin/activate


3. Install dependensi
bash
pip install -r requirements.txt


4. Konfigurasi variabel lingkungan
Buat file .env di direktori utama dengan variabel berikut:

MYSQL_HOST=localhost
MYSQL_USER=nama_pengguna_anda
MYSQL_PASSWORD=kata_sandi_anda
MYSQL_DATABASE=perpustakaan
ELASTICSEARCH_HOST=localhost
ELASTICSEARCH_PORT=9200


## Struktur Proyek

├── app.py              # File aplikasi utama Flask
├── database.py         # Konfigurasi dan pembuatan database
├── mysql_manager.py    # Manajemen operasi MySQL
├── elastic_manager.py  # Manajemen operasi Elasticsearch
├── templates/          # Template HTML
│   └── index.html     # Halaman utama
├── requirements.txt    # Dependensi proyek
└── README.md          # Dokumentasi proyek


## Menjalankan Aplikasi
bash
python app.py

Aplikasi akan tersedia di http://localhost:5000

## Endpoint API
- GET /: Halaman utama aplikasi
- POST /books: Menambah buku baru
  - Body: JSON dengan field (judul, penulis, tahun_terbit, penerbit, isbn, deskripsi)
- GET /books: Mendapatkan daftar semua buku
- GET /books/search?q=: Mencari buku berdasarkan kata kunci

## Struktur Database
### Tabel Books
- id (INT, AUTO_INCREMENT, PRIMARY KEY)
- judul (VARCHAR(255))
- penulis (VARCHAR(255))
- tahun_terbit (INT)
- penerbit (VARCHAR(255))
- isbn (VARCHAR(13))
- deskripsi (TEXT)
- created_at (TIMESTAMP)

## Konfigurasi Database
### MySQL
- Pastikan server MySQL berjalan
- Database akan dibuat otomatis saat pertama kali menjalankan aplikasi
- Tabel books akan dibuat otomatis dengan struktur yang diperlukan

### Elasticsearch
- Pastikan server Elasticsearch berjalan di port 9200
- Indeks akan dibuat otomatis saat menambahkan buku pertama

## Kontribusi
1. Fork repository
2. Buat branch fitur baru (git checkout -b fitur/FiturBaru)
3. Commit perubahan Anda (git commit -m 'Menambahkan Fitur Baru')
4. Push ke branch (git push origin fitur/FiturBaru)
5. Buat Pull Request

## Lisensi
Proyek ini dilisensikan di bawah Lisensi MIT - lihat file LICENSE untuk detail

## Ucapan Terima Kasih
- Flask Documentation
- MySQL Documentation
- Elasticsearch Documentation
