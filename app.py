from flask import Flask, jsonify, request
import sqlite3

app = Flask(__name__)

# Update database path to your location
DATABASE_PATH = '/Users/jannedahl/Desktop/Kod/SQL/mydatabase.db'

def get_db_connection():
    conn = sqlite3.connect(DATABASE_PATH)  # Use the correct path to your database
    conn.row_factory = sqlite3.Row
    return conn

@app.route('/api/makes', methods=['GET'])
def get_makes():
    conn = get_db_connection()
    makes = conn.execute('SELECT DISTINCT make FROM APITest').fetchall()  # Ensure it's accessing the correct table 'APITest'
    conn.close()
    makes_list = [make['make'] for make in makes]
    return jsonify({"makes": makes_list})

@app.route('/api/models', methods=['GET'])
def get_models():
    make = request.args.get('make')
    if not make:
        return jsonify({"error": "No make provided"}), 400
    
    conn = get_db_connection()
    models = conn.execute('SELECT model FROM APITest WHERE make = ?', (make,)).fetchall()  # Correct query for your table
    conn.close()
    
    models_list = [model['model'] for model in models]
    return jsonify({"models": models_list})

if __name__ == "__main__":
    app.run(debug=True)
