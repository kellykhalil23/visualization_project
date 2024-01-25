import os


# Get the base directory of the application
base_dir = os.path.abspath(os.path.dirname(__file__))

# Construct the path to the database file (assuming db is outside the app folder)
db_path = os.path.join(base_dir, "..", "db", "database.db")

print(db_path)