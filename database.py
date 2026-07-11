import sqlite3

DB_NAME = "resources.db"

# -----------------------------
# CONNECT DATABASE
# -----------------------------
def connect():
    return sqlite3.connect(DB_NAME)

# -----------------------------
# CREATE TABLES
# -----------------------------
def create_tables():
    conn = connect()
    cur = conn.cursor()

    # Hospitals
    cur.execute("""
    CREATE TABLE IF NOT EXISTS hospitals (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT,
        location TEXT,
        phone TEXT,
        map_link TEXT
    )
    """)

    # Blood Banks
    cur.execute("""
    CREATE TABLE IF NOT EXISTS bloodbanks (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT,
        location TEXT,
        phone TEXT,
        map_link TEXT
    )
    """)

    # NGOs
    cur.execute("""
    CREATE TABLE IF NOT EXISTS ngos (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT,
        location TEXT,
        phone TEXT,
        map_link TEXT
    )
    """)

    conn.commit()
    conn.close()


# -----------------------------
# INSERT DEFAULT DATA
# -----------------------------
def insert_sample_data():
    conn = connect()
    cur = conn.cursor()

    # Check if already exists
    cur.execute("SELECT COUNT(*) FROM hospitals")
    if cur.fetchone()[0] > 0:
        conn.close()
        return

    # -----------------------------
    # HOSPITALS (15+ Ballari)
    # -----------------------------
    hospitals = [
        ("VIMS Hospital", "Ballari", "08392-123456", "https://maps.google.com/?q=VIMS+Hospital+Ballari"),
        ("Sanjeevini Hospital", "Ballari", "9876543210", "https://maps.google.com/?q=Sanjeevini+Hospital+Ballari"),
        ("Basaveshwara Hospital", "Ballari", "9845123456", "https://maps.google.com/?q=Basaveshwara+Hospital+Ballari"),
        ("Ashwini Hospital", "Ballari", "9988776655", "https://maps.google.com/?q=Ashwini+Hospital+Ballari"),
        ("City Care Hospital", "Ballari", "9123456780", "https://maps.google.com/?q=City+Care+Hospital+Ballari"),
        ("Lifeline Hospital", "Ballari", "9012345678", "https://maps.google.com/?q=Lifeline+Hospital+Ballari"),
        ("Sai Hospital", "Ballari", "9090909090", "https://maps.google.com/?q=Sai+Hospital+Ballari"),
        ("Government Hospital", "Ballari", "0800000000", "https://maps.google.com/?q=Government+Hospital+Ballari"),
        ("Apollo Clinic", "Ballari", "8888888888", "https://maps.google.com/?q=Apollo+Clinic+Ballari"),
        ("Sri Lakshmi Hospital", "Ballari", "7777777777", "https://maps.google.com/?q=Sri+Lakshmi+Hospital+Ballari"),
        ("Aditya Hospital", "Ballari", "6666666666", "https://maps.google.com/?q=Aditya+Hospital+Ballari"),
        ("Om Hospital", "Ballari", "9555555555", "https://maps.google.com/?q=Om+Hospital+Ballari"),
        ("Care Plus Hospital", "Ballari", "9444444444", "https://maps.google.com/?q=Care+Plus+Hospital+Ballari"),
        ("Sunrise Hospital", "Ballari", "9333333333", "https://maps.google.com/?q=Sunrise+Hospital+Ballari"),
        ("Shanti Hospital", "Ballari", "9222222222", "https://maps.google.com/?q=Shanti+Hospital+Ballari")
    ]

    cur.executemany("INSERT INTO hospitals (name, location, phone, map_link) VALUES (?, ?, ?, ?)", hospitals)

    # -----------------------------
    # BLOOD BANKS
    # -----------------------------
    bloodbanks = [
        ("District Blood Bank", "Ballari", "9111111111", "https://maps.google.com/?q=Blood+Bank+Ballari"),
        ("Red Cross Blood Bank", "Ballari", "9222222222", "https://maps.google.com/?q=Red+Cross+Ballari"),
        ("Life Blood Center", "Ballari", "9333333333", "https://maps.google.com/?q=Blood+Center+Ballari"),
        ("City Blood Bank", "Ballari", "9444444444", "https://maps.google.com/?q=City+Blood+Bank+Ballari"),
        ("Health Blood Bank", "Ballari", "9555555555", "https://maps.google.com/?q=Health+Blood+Bank+Ballari"),
        ("Save Life Blood Bank", "Ballari", "9666666666", "https://maps.google.com/?q=Save+Life+Blood+Bank+Ballari"),
        ("Care Blood Bank", "Ballari", "9777777777", "https://maps.google.com/?q=Care+Blood+Bank+Ballari"),
        ("Emergency Blood Bank", "Ballari", "9888888888", "https://maps.google.com/?q=Emergency+Blood+Bank+Ballari"),
        ("Trust Blood Bank", "Ballari", "9999999999", "https://maps.google.com/?q=Trust+Blood+Bank+Ballari"),
        ("Hope Blood Bank", "Ballari", "9000000000", "https://maps.google.com/?q=Hope+Blood+Bank+Ballari")
    ]

    cur.executemany("INSERT INTO bloodbanks (name, location, phone, map_link) VALUES (?, ?, ?, ?)", bloodbanks)

    # -----------------------------
    # NGOS
    # -----------------------------
    ngos = [
        ("Helping Hands NGO", "Ballari", "9011111111", "https://maps.google.com/?q=Helping+Hands+Ballari"),
        ("Care Foundation", "Ballari", "9022222222", "https://maps.google.com/?q=Care+Foundation+Ballari"),
        ("Hope Trust", "Ballari", "9033333333", "https://maps.google.com/?q=Hope+Trust+Ballari"),
        ("Smile NGO", "Ballari", "9044444444", "https://maps.google.com/?q=Smile+NGO+Ballari"),
        ("Life Support NGO", "Ballari", "9055555555", "https://maps.google.com/?q=Life+Support+Ballari"),
        ("Humanity NGO", "Ballari", "9066666666", "https://maps.google.com/?q=Humanity+Ballari"),
        ("Save Life NGO", "Ballari", "9077777777", "https://maps.google.com/?q=Save+Life+Ballari"),
        ("Helping Society", "Ballari", "9088888888", "https://maps.google.com/?q=Helping+Society+Ballari"),
        ("Relief NGO", "Ballari", "9099999999", "https://maps.google.com/?q=Relief+Ballari"),
        ("Charity Trust", "Ballari", "9001111111", "https://maps.google.com/?q=Charity+Trust+Ballari")
    ]

    cur.executemany("INSERT INTO ngos (name, location, phone, map_link) VALUES (?, ?, ?, ?)", ngos)

    conn.commit()
    conn.close()


# -----------------------------
# FETCH DATA
# -----------------------------
def get_data(table):
    conn = connect()
    cur = conn.cursor()
    cur.execute(f"SELECT * FROM {table}")
    data = cur.fetchall()
    conn.close()
    return data


# -----------------------------
# ADD DATA (ADMIN)
# -----------------------------
def add_data(table, name, location, phone, map_link):
    conn = connect()
    cur = conn.cursor()

    cur.execute(
        f"INSERT INTO {table} (name, location, phone, map_link) VALUES (?, ?, ?, ?)",
        (name, location, phone, map_link)
    )

    conn.commit()
    conn.close()