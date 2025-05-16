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

## Persyaratan

- Python 3.7+
- MySQL Server
- Elasticsearch 7.x
- pip (Python package manager)

## Instalasi

1. Clone repositori ini:
```bash
git clone https://github.com/exelpratama13/Kelompok-6-UTS-Topik-Khusus.git
cd Kelompok-6-UTS-Topik-Khusus
```

2. Buat virtual environment Python:
```bash
python -m venv venv
source venv/bin/activate  # Linux/Mac
venv\Scripts\activate     # Windows
```

3. Install dependensi:
```bash
pip install -r requirements.txt
```

4. Buat file `.env` di root direktori dengan konfigurasi berikut:
```
MYSQL_HOST=localhost
MYSQL_USER=root
MYSQL_PASSWORD=your_password
MYSQL_DATABASE=book_library
ELASTICSEARCH_HOST=http://localhost:9200
```

5. Buat database MySQL:
```sql
CREATE DATABASE book_library;
```

## Menjalankan Aplikasi

1. Pastikan MySQL dan Elasticsearch sudah berjalan
2. Jalankan aplikasi:
```bash
python app.py
```
3. Buka browser dan akses `http://localhost:5000`

## Fitur

- Pencarian buku berdasarkan judul atau penulis
- Tampilan cover buku
- Informasi detail buku
- Penyimpanan data di MySQL
- Pencarian cepat menggunakan Elasticsearch

## Struktur Proyek

- `app.py` - File utama aplikasi Flask
- `database.py` - Konfigurasi dan pembuatan database
- `mysql_manager.py` - Manajer koneksi dan operasi MySQL
- `elastic_manager.py` - Manajer koneksi dan operasi Elasticsearch
- `templates/` - Direktori berisi template HTML
- `requirements.txt` - Daftar dependensi Python

## API Endpoints

- `GET /api/books/search?q=<query>` - Mencari buku
- `GET /api/books/<id>` - Mendapatkan detail buku
- `POST /api/books` - Menambah buku baru

## Contoh Request Menambah Buku

```bash
curl -X POST http://localhost:5000/api/books \
  -H "Content-Type: application/json" \
  -d '{
    "judul": "Judul Buku",
    "penulis": "Nama Penulis",
    "tahun_terbit": "Deskripsi buku",
    "penerbit": "https://example.com/cover.jpg"
    "isbn": "https://example.com/cover.jpg"
    "deskripsi": "https://example.com/cover.jpg"
  }'
```


