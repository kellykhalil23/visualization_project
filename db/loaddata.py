import sqlite3
import csv


def load_csv_data(database_path, csv_file_path):
    # Connect to the SQLite database
    conn = sqlite3.connect(database_path)
    cursor = conn.cursor()

    # Read data from the CSV file
    with open(csv_file_path, 'r') as csv_file:
        csv_reader = csv.reader(csv_file)
        next(csv_reader)  # Skip the header row if present

        for row in csv_reader:
            
          
            # Insert data into the  table
            cursor.execute('''
                INSERT INTO SUIS (CancerSite, AgeGroup0_5, AgeGroup5_10, AgeGroup10_15,
                                AgeGroup15_20, AgeGroup20_25, AgeGroup25_30, AgeGroup30_35,
                                AgeGroup35_40, AgeGroup40_45, AgeGroup45_50, AgeGroup50_55,
                                AgeGroup55_60, AgeGroup60_65, AgeGroup65_70, AgeGroup70_75,
                                AgeGroup75_80, AgeGroup80_85)
                VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
            ''', row)


    # Commit changes and close the connection
    conn.commit()
    conn.close()

    print(f"Data loaded from '{csv_file_path}' into 'your_table_name' table successfully.")

# Example usage:
database_path = 'database.db'
csv_file_path = '/root/dataviz/dataviz_project/data/SUIS.csv'  # Replace with the actual path to your CSV file


# Call load_csv_data to insert data from the CSV file
load_csv_data(database_path, csv_file_path)
