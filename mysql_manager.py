import mysql.connector
from dotenv import load_dotenv
import os

load_dotenv()

class MySQLManager:
    def __init__(self):
        self.connection = mysql.connector.connect(
            host=os.getenv('MYSQL_HOST'),
            user=os.getenv('MYSQL_USER'),
            password=os.getenv('MYSQL_PASSWORD'),
            database=os.getenv('MYSQL_DATABASE')
        )
        self.cursor = self.connection.cursor(dictionary=True)
    
    def add_book(self, book_data):
        query = """
            INSERT INTO books (judul, penulis, tahun_terbit, penerbit, isbn, deskripsi)
            VALUES (%(judul)s, %(penulis)s, %(tahun_terbit)s, %(penerbit)s, %(isbn)s, %(deskripsi)s)
        """
        self.cursor.execute(query, book_data)
        self.connection.commit()
        return self.cursor.lastrowid
    
    def get_book(self, book_id):
        query = "SELECT * FROM books WHERE id = %s"
        self.cursor.execute(query, (book_id,))
        return self.cursor.fetchone()
    
    def close(self):
        self.cursor.close()
        self.connection.close()