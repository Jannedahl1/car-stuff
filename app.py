from flask import Flask, jsonify
from flask_cors import CORS  # This is for handling cross-origin requests
import sqlite3

app = Flask(__name__)
CORS(app)  # Enable CORS for all routes

# Database path
DB_PATH = '/Users/jannedahl/Desktop/Kod/SQL/mydatabase.db'  # Adjust this path as necessary

# Route to get car makes and models
@app.route('/api/cars', methods=['GET'])
def get_cars():
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    cursor.execute("SELECT make, model FROM APITest")
    rows = cursor.fetchall()
    conn.close()
    
    # Prepare data to send back as JSON
    cars = [{'make': row[0], 'model': row[1]} for row in rows]
    return jsonify(cars)

if __name__ == '__main__':
    app.run(debug=True)  # This will run the Flask server locally
