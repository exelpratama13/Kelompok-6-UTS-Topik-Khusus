import mysql.connector
from dotenv import load_dotenv
import os

load_dotenv()

def create_database():
    connection = mysql.connector.connect(
        host=os.getenv('MYSQL_HOST'),
        user=os.getenv('MYSQL_USER'),
        password=os.getenv('MYSQL_PASSWORD')
    )
    cursor = connection.cursor()
    
    # Buat database jika belum ada
    cursor.execute("CREATE DATABASE IF NOT EXISTS {}".format(os.getenv('MYSQL_DATABASE')))
    
    # Gunakan database
    cursor.execute("USE {}".format(os.getenv('MYSQL_DATABASE')))
    
    # Buat tabel books
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS books (
            id INT AUTO_INCREMENT PRIMARY KEY,
            judul VARCHAR(255) NOT NULL,
            penulis VARCHAR(255) NOT NULL,
            tahun_terbit INT,
            penerbit VARCHAR(255),
            isbn VARCHAR(13),
            deskripsi TEXT,
            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        )
    """)
    
    connection.commit()
    connection.close()