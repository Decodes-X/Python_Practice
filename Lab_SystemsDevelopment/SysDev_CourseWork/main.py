from flask import Flask, render_template
from db import get_connection
app = Flask(__name__)

@app.route("/")
def home():
    return render_template('home.html')

if __name__ == "__main__":
    app.run(debug=True)

def check_db_conn():
    with get_connection() as conn:
        with conn.cursor() as cur:
            cur.execute("SELECT 1")
            result = cur.fetchone()
            return result is not None

    return jsonify({"status": "Database connection successful" if check_db_conn() else "Database connection failed"})

if __name__ == "__main__":
    app.run()


def create_student_table():
    with get_connection() as conn:
        with conn.cursor() as cur:
            cur.execute("""
                CREATE TABLE IF NOT EXISTS students (
                    id SERIAL PRIMARY KEY,
                    name VARCHAR(100) NOT NULL,
                    age INT NOT NULL,
                    grade VARCHAR(10) NOT NULL
                )
            """)
            conn.commit()