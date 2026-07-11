from flask import Flask, render_template, request, redirect
import sqlite3

app = Flask(__name__)

def get_db():
    conn = sqlite3.connect("resources.db")
    conn.row_factory = sqlite3.Row
    return conn

# CREATE TABLES
def create_tables():
    conn = get_db()

    conn.execute("""
    CREATE TABLE IF NOT EXISTS hospitals (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT,
        location TEXT,
        phone TEXT
    )
    """)

    conn.execute("""
    CREATE TABLE IF NOT EXISTS bloodbanks (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT,
        location TEXT,
        phone TEXT
    )
    """)

    conn.execute("""
    CREATE TABLE IF NOT EXISTS ngos (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT,
        location TEXT,
        phone TEXT
    )
    """)

    conn.commit()
    conn.close()

create_tables()

# HOME
@app.route("/")
def home():
    return render_template("index.html")

# ---------------- HOSPITALS ----------------
@app.route("/hospitals")
def hospitals():
    conn = get_db()
    data = conn.execute("SELECT * FROM hospitals").fetchall()
    conn.close()
    return render_template("hospitals.html", data=data, title="HOSPITALS")

@app.route("/add_hospital", methods=["POST"])
def add_hospital():
    conn = get_db()
    conn.execute("INSERT INTO hospitals (name, location, phone) VALUES (?, ?, ?)",
                 (request.form["name"], request.form["location"], request.form["phone"]))
    conn.commit()
    conn.close()
    return redirect("/hospitals")

@app.route("/delete_hospital/<int:id>")
def delete_hospital(id):
    conn = get_db()
    conn.execute("DELETE FROM hospitals WHERE id=?", (id,))
    conn.commit()
    conn.close()
    return redirect("/hospitals")

# ---------------- BLOOD BANKS ----------------
@app.route("/bloodbanks")
def bloodbanks():
    conn = get_db()
    data = conn.execute("SELECT * FROM bloodbanks").fetchall()
    conn.close()
    return render_template("hospitals.html", data=data, title="BLOOD BANKS")

@app.route("/add_bloodbank", methods=["POST"])
def add_bloodbank():
    conn = get_db()
    conn.execute("INSERT INTO bloodbanks (name, location, phone) VALUES (?, ?, ?)",
                 (request.form["name"], request.form["location"], request.form["phone"]))
    conn.commit()
    conn.close()
    return redirect("/bloodbanks")

@app.route("/delete_bloodbank/<int:id>")
def delete_bloodbank(id):
    conn = get_db()
    conn.execute("DELETE FROM bloodbanks WHERE id=?", (id,))
    conn.commit()
    conn.close()
    return redirect("/bloodbanks")

# ---------------- NGOS ----------------
@app.route("/ngos")
def ngos():
    conn = get_db()
    data = conn.execute("SELECT * FROM ngos").fetchall()
    conn.close()
    return render_template("hospitals.html", data=data, title="NGOs")

@app.route("/add_ngo", methods=["POST"])
def add_ngo():
    conn = get_db()
    conn.execute("INSERT INTO ngos (name, location, phone) VALUES (?, ?, ?)",
                 (request.form["name"], request.form["location"], request.form["phone"]))
    conn.commit()
    conn.close()
    return redirect("/ngos")

@app.route("/delete_ngo/<int:id>")
def delete_ngo(id):
    conn = get_db()
    conn.execute("DELETE FROM ngos WHERE id=?", (id,))
    conn.commit()
    conn.close()
    return redirect("/ngos")

# RUN
if __name__ == "__main__":
    app.run(debug=True)