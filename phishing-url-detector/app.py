from flask import Flask, render_template, request
from detector import detect_phishing
import sqlite3
from datetime import datetime

app = Flask(__name__)

def init_db():
    conn = sqlite3.connect("database.db")
    c = conn.cursor()
    c.execute('''CREATE TABLE IF NOT EXISTS history (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                url TEXT,
                result TEXT,
                score INTEGER,
                date TEXT)''')
    conn.commit()
    conn.close()

def save_to_db(url, result, score):
    conn = sqlite3.connect("database.db")
    c = conn.cursor()
    c.execute("INSERT INTO history VALUES (NULL, ?, ?, ?, ?)",
              (url, result, score, datetime.now().strftime("%Y-%m-%d %H:%M:%S")))
    conn.commit()
    conn.close()

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        url = request.form["url"]
        result, score, features = detect_phishing(url)
        save_to_db(url, result, score)
        return render_template("result.html",
                               url=url,
                               result=result,
                               score=score,
                               features=features)
    return render_template("index.html")

@app.route("/history")
def history():
    conn = sqlite3.connect("database.db")
    c = conn.cursor()
    c.execute("SELECT * FROM history ORDER BY id DESC")
    rows = c.fetchall()
    conn.close()
    return render_template("history.html", rows=rows)

if __name__ == "__main__":
    init_db()
    app.run(debug=True)