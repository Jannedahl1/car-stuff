from flask import Flask, jsonify, request
import sqlite3

app = Flask(__name__)

# Database connection
def get_db_connection():
    conn = sqlite3.connect('mydatabase.db')  # Replace with the correct path to your database
    conn.row_factory = sqlite3.Row
    return conn

# Fetch car makes (distinct makes)
@app.route('/api/makes', methods=['GET'])
def get_makes():
    conn = get_db_connection()
    makes = conn.execute('SELECT DISTINCT make FROM APITest').fetchall()
    conn.close()
    makes_list = [make['make'] for make in makes]
    return jsonify({"makes": makes_list})

@app.route('/api/models', methods=['GET'])
def get_models():
    make = request.args.get('make')
    if not make:
        return jsonify({"error": "No make provided"}), 400
    
    conn = get_db_connection()
    models = conn.execute('SELECT model FROM APITest WHERE make = ?', (make,)).fetchall()
    conn.close()
    
    models_list = [model['model'] for model in models]
    return jsonify({"models": models_list})

