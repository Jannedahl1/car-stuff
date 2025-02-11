from flask import Flask, jsonify, request
import sqlite3

app = Flask(__name__)

# Define the database path
db_path = "/Users/jannedahl/Desktop/Kod/SQL/mydatabase.db"

@app.route("/api/makes")
def get_makes():
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()

    # Get distinct makes from the database
    cursor.execute("SELECT DISTINCT make FROM APITest")
    makes = [row[0] for row in cursor.fetchall()]

    conn.close()
    return jsonify({"makes": makes})

@app.route("/api/models")
def get_models():
    make = request.args.get('make')
    if make:
        conn = sqlite3.connect(db_path)
        cursor = conn.cursor()

        # Get all models for the selected make
        cursor.execute("SELECT model FROM APITest WHERE make = ?", (make,))
        models = [row[0] for row in cursor.fetchall()]

        conn.close()
        return jsonify({"models": models})
    return jsonify({"models": []})

if __name__ == "__main__":
    app.run(debug=True)
