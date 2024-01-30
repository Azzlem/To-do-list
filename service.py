from datetime import datetime

import psycopg2

from config.settings import query_insert, query_create, query_select_false, query_select_true


def connect_to_db():
    conn = psycopg2.connect(dbname="To-do-list", user="postgres", password="postgres", host="localhost", port="5432")
    cur = conn.cursor()
    return conn, cur


def create_base_if_not_exists():
    conn, cur = connect_to_db()
    cur.execute(query_create)
    conn.commit()
    cur.close
    conn.close()
    print("Таблица people успешно создана")


def get_values(name: str, description: str, bool: bool):
    date_now = datetime.now()
    values = (name, description, bool, date_now)
    return values


def insert_values(values: tuple):
    conn, cur = connect_to_db()
    query = query_insert
    cur.execute(query, values)
    conn.commit()
    cur.close
    conn.close()


def select_values(answer: bool):
    conn, cur = connect_to_db()
    if answer:
        query = query_select_true

    else:
        query = query_select_false
    cur.execute(query)
    rows = cur.fetchall()

    cur.close
    conn.close()
    return rows
