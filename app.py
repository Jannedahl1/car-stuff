from flask import Flask, jsonify
import sqlite3

app = Flask(__name__)

# Database path
DB_PATH = '/Users/jannedahl/Desktop/Kod/SQL/mydatabase.db'  # Adjust the path

# Route to get car makes and models
@app.route('/api/cars', methods=['GET'])
def get_cars():
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    cursor.execute("SELECT make, model FROM APITest")
    rows = cursor.fetchall()
    conn.close()
    
    # Return the rows in JSON format
    cars = [{'make': row[0], 'model': row[1]} for row in rows]
    return jsonify(cars)

if __name__ == '__main__':
    app.run(debug=True)
