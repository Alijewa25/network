import sqlite3
from os import path

ROOT = path.dirname(path.abspath(__file__))
DB_PATH = path.join(ROOT, 'database.db')


def init_db():
    if not path.exists(DB_PATH):
        con = sqlite3.connect(DB_PATH)
        cur = con.cursor()
        schema_file = path.join(ROOT, 'schema.sql')
        if path.exists(schema_file):
            with open(schema_file, 'r') as f:
                cur.executescript(f.read())
        else:
            cur.execute(
                'create table if not exists posts (id integer primary key autoincrement, name text not null, content text not null)'
            )
        con.commit()
        con.close()


def create_post(name, content):
    con = sqlite3.connect(DB_PATH)
    cur = con.cursor()
    cur.execute('insert into posts (name, content) values (?, ?)', (name, content))
    con.commit()
    con.close()


def get_posts():
    con = sqlite3.connect(DB_PATH)
    cur = con.cursor()
    cur.execute('select id, name, content from posts order by id desc')
    rows = cur.fetchall()
    con.close()
    return [{'id': r[0], 'name': r[1], 'content': r[2]} for r in rows]