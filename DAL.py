import sqlite3


def connect():
    connection = sqlite3.connect("books.db")
    cur = connection.cursor()
    cur.execute(
        "CREATE TABLE IF NOT EXISTS book (id INTEGER PRIMARY KEY, title text, author text, year INTEGER, ISBN INTEGER)")
    connection.commit()
    connection.close()


def insert(title, author, year, ISBN):
    connection = sqlite3.connect("books.db")
    cur = connection.cursor()
    cur.execute("INSERT INTO book VALUES (NULL, ?, ?, ?, ?)",
                (title, author, year, ISBN))
    connection.commit()
    connection.close()


def view():
    connection = sqlite3.connect("books.db")
    cur = connection.cursor()
    cur.execute("SELECT * FROM book")
    records = cur.fetchall()
    connection.close()
    return records


def search(title='', author='', year='', ISBN=''):
    connection = sqlite3.connect("books.db")
    cur = connection.cursor()
    cur.execute("SELECT * FROM book WHERE title=? OR author=? OR year=? OR ISBN=?",
                (title, author, year, ISBN))
    records = cur.fetchall()
    connection.close()
    return records


def delete(id):
    connection = sqlite3.connect("books.db")
    cur = connection.cursor()
    cur.execute("DELETE FROM book WHERE id=?", (id,))
    connection.commit()
    connection.close()


def update(id, title, author, year, ISBN):
    connection = sqlite3.connect("books.db")
    cur = connection.cursor()
    cur.execute("UPDATE book SET title=?, author=?, year=?, isbn=? WHERE id=?",
                (title, author, year, ISBN, id))
    connection.commit()
    connection.close()


connect()
