import sqlite3

def log_query(case_type, number, year, response):
    conn = sqlite3.connect("database.db")
    c = conn.cursor()

    # Create table if not exists
    c.execute('''
        CREATE TABLE IF NOT EXISTS logs (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            case_type TEXT,
            case_number TEXT,
            filing_year TEXT,
            response TEXT
        )
    ''')

    # Insert log entry
    c.execute(
        "INSERT INTO logs (case_type, case_number, filing_year, response) VALUES (?, ?, ?, ?)",
        (case_type, number, year, str(response))
    )

    conn.commit()
    conn.close()
