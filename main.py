import sqlite3
from pprint import pprint

with sqlite3.connect('book_store.sqlite3') as connection:
    cursor = connection.cursor()
    query = """
        CREATE TABLE IF NOT EXISTS authors(
            id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
            authors_name TEXT NOT NULL,
            year_of_birth INTEGER NOT NULL
        );
    """
    cursor.execute(query)
    another_table = """
        CREATE TABLE IF NOT EXISTS books(
            id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
            author_id INTEGER NOT NULL,
            price FLOAT CHECK (price > 0),
            description TEXT,
            FOREIGN KEY (author_id) REFERENCES authors(id)
        );             
    """
    cursor.execute(another_table)
    insert_query = """
        INSERT INTO authors (authors_name, year_of_birth)
        VALUES (?, ?)
    """
    cursor.execute(insert_query, ["Adam Mickiewicz", 1798])
    authors = [
        ("William Shakespeare", 1564),
        ("Agatha Christie", 1890),
        ("Barbara Cartland", 1901),
        ("Julia Child", 1912)
    ]
    cursor.executemany(insert_query, authors)
    read_query = """
        SELECT description
        FROM books
        WHERE (description LIKE "%Рецепт%")
    """
    result = cursor.execute(read_query)
    # pprint(result.fetchall(), indent=5)
    read_query2 = """
        SELECT description
        FROM books
        LIMIT 2
        OFFSET 1
    """
    result2 = cursor.execute(read_query2)
    pprint(result2.fetchall(), indent=1)
