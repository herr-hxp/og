import sqlite3
from flask import Flask, render_template

app = Flask(__name__)

def get_db_connection():
    conn = sqlite3.connect('database.db')
    conn.row_factory = sqlite3.Row
    return conn

@app.route('/')
def index():
    conn = get_db_connection()
    flavors = conn.execute('SELECT * FROM flavors').fetchall()
    storage = conn.execute('SELECT * FROM storage').fetchall()
    network = conn.execute('SELECT * FROM network').fetchall()
    licenses = conn.execute('SELECT * FROM licenses').fetchall()
    conn.close()
    return render_template('index.html', flavors=flavors, network=network, licenses=licenses, storage=storage)

#if __name__ == "__main__":
#    app.run(host="0.0.0.0", port=5000, debug=True)
