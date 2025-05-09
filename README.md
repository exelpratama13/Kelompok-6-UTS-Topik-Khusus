# Sistem Manajemen Buku dengan Elasticsearch dan MySQL

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

## Persyaratan Sistem
1. Python 3.x
2. MySQL Server 8.x
3. Elasticsearch 7.x
4. Git
5. Virtual Environment (venv)

## Langkah-langkah Instalasi

### 1. Persiapan Awal
bash
# Clone repository
git clone [url-repository]
cd sistem-manajemen-perpustakaan

# Buat virtual environment
python -m venv venv

# Aktifkan virtual environment
# Untuk Windows:
venv\Scripts\activate
# Untuk Linux/Mac:
source venv/bin/activate


### 2. Instalasi Dependensi
bash
# Upgrade pip
python -m pip install --upgrade pip

# Install semua dependensi
pip install -r requirements.txt


### 3. Konfigurasi Database

#### MySQL
1. Pastikan MySQL Server sudah terinstall dan berjalan
2. Buat file .env di root project dengan isi:
env
MYSQL_HOST=localhost
MYSQL_USER=nama_pengguna_anda
MYSQL_PASSWORD=kata_sandi_anda
MYSQL_DATABASE=perpustakaan
ELASTICSEARCH_HOST=localhost
ELASTICSEARCH_PORT=9200


#### Elasticsearch
1. Download dan install Elasticsearch 7.x
2. Pastikan Elasticsearch berjalan di port 9200
3. Buka browser dan akses http://localhost:9200 untuk memastikan Elasticsearch berjalan

### 4. Menjalankan Aplikasi
bash
# Pastikan virtual environment aktif
# Jalankan aplikasi
python app.py


Aplikasi akan berjalan di http://localhost:5000

## Struktur Proyek

├── app.py              # File aplikasi utama Flask
├── database.py         # Konfigurasi dan pembuatan database
├── mysql_manager.py    # Manajemen operasi MySQL
├── elastic_manager.py  # Manajemen operasi Elasticsearch
├── templates/          # Template HTML
│   └── index.html     # Halaman utama
├── requirements.txt    # Dependensi proyek
└── README.md          # Dokumentasi proyek


## Penggunaan API

### 1. Menambah Buku Baru
bash
POST /books
Content-Type: application/json

{
    "judul": "Judul Buku",
    "penulis": "Nama Penulis",
    "tahun_terbit": 2024,
    "penerbit": "Nama Penerbit",
    "isbn": "9781234567890",
    "deskripsi": "Deskripsi buku"
}


### 2. Melihat Semua Buku
bash
GET /books


### 3. Mencari Buku
bash
GET /books/search?q=kata_kunci


## Struktur Database

### Tabel Books
| Kolom | Tipe Data | Keterangan |
|-------|-----------|------------|
| id | INT | Primary Key, Auto Increment |
| judul | VARCHAR(255) | Judul buku |
| penulis | VARCHAR(255) | Nama penulis |
| tahun_terbit | INT | Tahun terbit buku |
| penerbit | VARCHAR(255) | Nama penerbit |
| isbn | VARCHAR(13) | Nomor ISBN |
| deskripsi | TEXT | Deskripsi buku |
| created_at | TIMESTAMP | Waktu pembuatan record |

## Troubleshooting

### 1. Masalah Koneksi MySQL
- Pastikan MySQL Server berjalan
- Periksa kredensial di file .env
- Pastikan database perpustakaan sudah dibuat

### 2. Masalah Elasticsearch
- Pastikan Elasticsearch berjalan di port 9200
- Periksa log Elasticsearch untuk error
- Pastikan memori cukup untuk menjalankan Elasticsearch

### 3. Masalah Aplikasi
- Pastikan semua dependensi terinstall
- Periksa log aplikasi untuk error
- Pastikan virtual environment aktif

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
