from flask import Flask, request, jsonify, render_template
from mysql_manager import MySQLManager
from elastic_manager import ElasticManager
from database import create_database

app = Flask(__name__)
elastic_manager = ElasticManager()

# Buat database dan tabel jika belum ada
create_database()

@app.route('/books', methods=['POST'])
def add_book():
    data = request.json
    mysql_manager = MySQLManager()
    
    try:
        # Simpan ke MySQL
        book_id = mysql_manager.add_book(data)
        
        # Ambil data lengkap buku
        book = mysql_manager.get_book(book_id)
        
        # Indeks ke Elasticsearch
        elastic_manager.index_book(book)
        
        return jsonify({"message": "Buku berhasil ditambahkan", "book": book}), 201
    
    except Exception as e:
        return jsonify({"error": str(e)}), 500
    
    finally:
        mysql_manager.close()

@app.route('/books/search', methods=['GET'])
def search_books():
    query = request.args.get('q', '')
    if not query:
        return jsonify({"error": "Parameter pencarian tidak boleh kosong"}), 400
    
    try:
        # Cari menggunakan Elasticsearch
        results = elastic_manager.search_books(query)
        return jsonify({"results": results})
    
    except Exception as e:
        return jsonify({"error": str(e)}), 500

@app.route('/books', methods=['GET'])
def get_books():
    mysql_manager = MySQLManager()
    try:
        # Ambil semua buku dari MySQL
        query = "SELECT * FROM books"
        mysql_manager.cursor.execute(query)
        books = mysql_manager.cursor.fetchall()
        return jsonify({"books": books})
    except Exception as e:
        return jsonify({"error": str(e)}), 500
    finally:
        mysql_manager.close()

@app.route('/')
def index():
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)