import sqlite3

from collections import namedtuple

ReaderTuple = namedtuple('Reader', 'id name')
EndpointTuple = namedtuple('Endpoint', 'reader_id time activity end')


def readertuple_factory(cursor, row):
    return ReaderTuple(*row)


def select_all_readers(conn):
    conn.row_factory = readertuple_factory
    cur = conn.cursor()
    cur.execute("SELECT * FROM reader")

    return cur.fetchall()


def create_connection():
    conn = None
    try:
        conn = sqlite3.connect('screentime.db')

    except Exception as e:
        print(e)

    return conn


def insert_endpoint(conn, endpoint):
    print(endpoint)
