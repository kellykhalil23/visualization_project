import sqlite3

def create_users_table(db_file):
    try:
        # Connect to the SQLite database
        conn = sqlite3.connect(db_file)
        cursor = conn.cursor()

        # Create the USA table
        cursor.execute('''
             CREATE TABLE USA (
                CancerSite TEXT PRIMARY KEY,
                AgeGroup0_5 REAL,
                AgeGroup5_10 REAL,
                AgeGroup10_15 REAL,
                AgeGroup15_20 REAL,
                AgeGroup20_25 REAL,
                AgeGroup25_30 REAL,
                AgeGroup30_35 REAL,
                AgeGroup35_40 REAL,
                AgeGroup40_45 REAL,
                AgeGroup45_50 REAL,
                AgeGroup50_55 REAL,
                AgeGroup55_60 REAL,
                AgeGroup60_65 REAL,
                AgeGroup65_70 REAL,
                AgeGroup70_75 REAL,
                AgeGroup75_80 REAL,
                AgeGroup80_85 REAL  
            )                 
        ''')

        # Create the GERMANY table
        cursor.execute('''
             CREATE TABLE GERMANY (
                CancerSite TEXT PRIMARY KEY,
                AgeGroup0_5 REAL,
                AgeGroup5_10 REAL,
                AgeGroup10_15 REAL,
                AgeGroup15_20 REAL,
                AgeGroup20_25 REAL,
                AgeGroup25_30 REAL,
                AgeGroup30_35 REAL,
                AgeGroup35_40 REAL,
                AgeGroup40_45 REAL,
                AgeGroup45_50 REAL,
                AgeGroup50_55 REAL,
                AgeGroup55_60 REAL,
                AgeGroup60_65 REAL,
                AgeGroup65_70 REAL,
                AgeGroup70_75 REAL,
                AgeGroup75_80 REAL,
                AgeGroup80_85 REAL  
            )                 
        ''')

        # Commit the changes (creating the table)
        conn.commit()
        print("Table 'users' created successfully.")

    except sqlite3.Error as e:
        print("SQLite error:", e)

    finally:
        # Close the connection, whether an exception occurred or not
        if conn:
            conn.close()

# Specify the name of your SQLite database file
db_file = "/root/dataviz/visualization_project/database.db"

# Call the function to create the 'users' table
create_users_table(db_file)
