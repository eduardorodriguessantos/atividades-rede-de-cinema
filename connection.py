import sqlite3

class Connection:
    @staticmethod
    def get_connection():
        conn = sqlite3.connect('cinema.db')
        return conn