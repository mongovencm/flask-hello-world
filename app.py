from flask import Flask
app = Flask(__name__)

import psycopg2

DB_URL = "postgresql://cmongo_3308_db_user:U4YxaCsJByx4VpqiMwph1MliAn0FVtbx@dpg-d7ar146dqaus73c2ch8g-a/cmongo_3308_db"

@app.route('/')
def hello_world():
    return 'Hello, World!'

@app.route('/db_test')
def testing():
    conn = psycopg2.connect(DB_URL)
    conn.close()
    return "Database Connection Successful!"

@app.route('/db_create')
def creating():
    conn = psycopg2.connect(DB_URL)
    cur = conn.cursor()
    cur.execute('''
        CREATE TABLE IF NOT EXISTS Basketball(
            First varchar(255),
            Last varchar(255),
            City varchar(255),
            Name varchar(255),
            Number int
        );
    ''')
    conn.commit()
    conn.close()

    return "Basketball Table Successfully Created"