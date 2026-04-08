from flask import Flask
app = Flask(__name__)

import psycopg2

@app.route('/')
def hello_world():
    return 'Hello, World!'

@app.route('/db_test')
def testing():
    conn = psycopg2.connect("postgresql://cmongo_3308_db_user:U4YxaCsJByx4VpqiMwph1MliAn0FVtbx@dpg-d7ar146dqaus73c2ch8g-a/cmongo_3308_db")
    conn.close()
    return "Database Connection Successful!"

