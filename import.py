import requests
import sqlite3

# Define the database path (adjust to your actual file location)
db_path = "/Users/jannedahl/Desktop/Kod/SQL/mydatabase.db"  # Ensure this path is correct
conn = sqlite3.connect(db_path)
cursor = conn.cursor()

# List of makes to fetch
makes = ["Audi", "BMW"]

# Loop through makes and fetch models for each
for make in makes:
    models_url = f"https://vpic.nhtsa.dot.gov/api/vehicles/GetModelsForMake/{make}?format=json"
    model_response = requests.get(models_url)
    
    if model_response.status_code == 200:
        models_data = model_response.json()["Results"]
        
        # Loop through each model and insert into the database
        for model_entry in models_data:
            model = model_entry["Model_Name"]
            year = 2020  # Set the year to 2020 for all models
            
            print(f"Inserting {make} {model} ({year}) into APITest")
            cursor.execute("INSERT INTO APITest (make, model, year) VALUES (?, ?, ?)", (make, model, year))
    
    else:
        print(f"Failed to fetch models for {make}")

# Commit and close
conn.commit()
conn.close()
print("Database updated with Audi and BMW models, all set to year 2020!")
