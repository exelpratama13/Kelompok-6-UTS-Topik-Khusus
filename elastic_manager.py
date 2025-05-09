from elasticsearch import Elasticsearch
from dotenv import load_dotenv
import os

load_dotenv()

class ElasticManager:
    def __init__(self):
        self.es = Elasticsearch([{
            'host': os.getenv('ELASTICSEARCH_HOST'),
            'port': int(os.getenv('ELASTICSEARCH_PORT'))
        }])

        # Cek dan buat index jika belum ada
        if not self.es.indices.exists(index='books'):
            self.create_index()

    def create_index(self):
        self.es.indices.create(index='books', body={
            "settings": {
                "analysis": {
                    "tokenizer": {
                        "edge_ngram_tokenizer": {
                            "type": "edge_ngram",
                            "min_gram": 1,
                            "max_gram": 20,
                            "token_chars": ["letter", "digit"]
                        }
                    },
                    "analyzer": {
                        "edge_ngram_analyzer": {
                            "type": "custom",
                            "tokenizer": "edge_ngram_tokenizer",
                            "filter": ["lowercase"]
                        }
                    }
                }
            },
            "mappings": {
                "properties": {
                    "id": {"type": "integer"},
                    "judul": {
                        "type": "text",
                        "analyzer": "edge_ngram_analyzer",
                        "search_analyzer": "standard"
                    },
                    "penulis": {
                        "type": "text",
                        "analyzer": "edge_ngram_analyzer",
                        "search_analyzer": "standard"
                    },
                    "tahun_terbit": {"type": "integer"},
                    "penerbit": {"type": "text"},
                    "isbn": {"type": "keyword"},
                    "deskripsi": {"type": "text"}
                }
            }
        })

    def index_book(self, book):
        self.es.index(index='books', id=book['id'], body=book)

    def search_books(self, query):
        body = {
            'query': {
                'multi_match': {
                    'query': query,
                    'fields': ['judul', 'penulis'],
                    'fuzziness': 'AUTO'
                }
            }
        }
        result = self.es.search(index='books', body=body)
        return [hit['_source'] for hit in result['hits']['hits']]
