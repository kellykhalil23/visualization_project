from flask import Flask, render_template, request, jsonify
from flask_sqlalchemy import SQLAlchemy
import sqlite3
from apiflask import APIFlask
import os

app = APIFlask(__name__, title="Demographic Cancer Crude Rates")

# Get the base directory of the application
base_dir = os.path.abspath(os.path.dirname(__file__))

# Construct the path to the database file (assuming db is outside the app folder)
db_path = os.path.join(base_dir, "..", "db", "database.db")

# Configure the SQLite database URI. Change the database URL as needed.
app.config['SQLALCHEMY_DATABASE_URI'] = f"sqlite:///{db_path}"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

class GERMANY(db.Model):
    __tablename__ = 'GERMANY'
    CancerSite = db.Column(db.TEXT, primary_key=True)
    AgeGroup0_5 = db.Column(db.REAL)
    AgeGroup5_10 = db.Column(db.REAL)
    AgeGroup10_15 = db.Column(db.REAL)
    AgeGroup15_20 = db.Column(db.REAL)
    AgeGroup20_25 = db.Column(db.REAL)
    AgeGroup25_30 = db.Column(db.REAL)
    AgeGroup30_35 = db.Column(db.REAL)
    AgeGroup35_40 = db.Column(db.REAL)
    AgeGroup40_45 = db.Column(db.REAL)
    AgeGroup45_50 = db.Column(db.REAL)
    AgeGroup50_55 = db.Column(db.REAL)
    AgeGroup55_60 = db.Column(db.REAL)
    AgeGroup60_65 = db.Column(db.REAL)
    AgeGroup65_70 = db.Column(db.REAL)
    AgeGroup70_75 = db.Column(db.REAL)
    AgeGroup75_80 = db.Column(db.REAL)
    AgeGroup80_85 = db.Column(db.REAL)

class CANADA(db.Model):
    __tablename__ = 'CANADA'
    CancerSite = db.Column(db.TEXT, primary_key=True)
    AgeGroup0_5 = db.Column(db.REAL)
    AgeGroup5_10 = db.Column(db.REAL)
    AgeGroup10_15 = db.Column(db.REAL)
    AgeGroup15_20 = db.Column(db.REAL)
    AgeGroup20_25 = db.Column(db.REAL)
    AgeGroup25_30 = db.Column(db.REAL)
    AgeGroup30_35 = db.Column(db.REAL)
    AgeGroup35_40 = db.Column(db.REAL)
    AgeGroup40_45 = db.Column(db.REAL)
    AgeGroup45_50 = db.Column(db.REAL)
    AgeGroup50_55 = db.Column(db.REAL)
    AgeGroup55_60 = db.Column(db.REAL)
    AgeGroup60_65 = db.Column(db.REAL)
    AgeGroup65_70 = db.Column(db.REAL)
    AgeGroup70_75 = db.Column(db.REAL)
    AgeGroup75_80 = db.Column(db.REAL)
    AgeGroup80_85 = db.Column(db.REAL)

class SUIS(db.Model):
    __tablename__ = 'SUIS'
    CancerSite = db.Column(db.TEXT, primary_key=True)
    AgeGroup0_5 = db.Column(db.REAL)
    AgeGroup5_10 = db.Column(db.REAL)
    AgeGroup10_15 = db.Column(db.REAL)
    AgeGroup15_20 = db.Column(db.REAL)
    AgeGroup20_25 = db.Column(db.REAL)
    AgeGroup25_30 = db.Column(db.REAL)
    AgeGroup30_35 = db.Column(db.REAL)
    AgeGroup35_40 = db.Column(db.REAL)
    AgeGroup40_45 = db.Column(db.REAL)
    AgeGroup45_50 = db.Column(db.REAL)
    AgeGroup50_55 = db.Column(db.REAL)
    AgeGroup55_60 = db.Column(db.REAL)
    AgeGroup60_65 = db.Column(db.REAL)
    AgeGroup65_70 = db.Column(db.REAL)
    AgeGroup70_75 = db.Column(db.REAL)
    AgeGroup75_80 = db.Column(db.REAL)
    AgeGroup80_85 = db.Column(db.REAL)

class USA(db.Model):
    __tablename__ = 'USA'
    CancerSite = db.Column(db.TEXT, primary_key=True)
    AgeGroup0_5 = db.Column(db.REAL)
    AgeGroup5_10 = db.Column(db.REAL)
    AgeGroup10_15 = db.Column(db.REAL)
    AgeGroup15_20 = db.Column(db.REAL)
    AgeGroup20_25 = db.Column(db.REAL)
    AgeGroup25_30 = db.Column(db.REAL)
    AgeGroup30_35 = db.Column(db.REAL)
    AgeGroup35_40 = db.Column(db.REAL)
    AgeGroup40_45 = db.Column(db.REAL)
    AgeGroup45_50 = db.Column(db.REAL)
    AgeGroup50_55 = db.Column(db.REAL)
    AgeGroup55_60 = db.Column(db.REAL)
    AgeGroup60_65 = db.Column(db.REAL)
    AgeGroup65_70 = db.Column(db.REAL)
    AgeGroup70_75 = db.Column(db.REAL)
    AgeGroup75_80 = db.Column(db.REAL)
    AgeGroup80_85 = db.Column(db.REAL)


@app.route('/create_table', methods=['POST'])
def create_cancer_table():
    # Get data from the request
    data = request.get_json()

    # Validate input
    if not isinstance(data, list) or len(data) < 2 or not all(isinstance(d, dict) for d in data[1:]):
        return jsonify({"error": "Invalid input format"}), 400

    # Connect to SQLite database
    conn = sqlite3.connect('/root/dataviz/dataviz_project/db/database.db')
    cursor = conn.cursor()

    try:
        country = data[0].get("Country")
        # Create table for the specified country
        cursor.execute(f'''
            CREATE TABLE IF NOT EXISTS "{country}" (
                "CancerSite" TEXT NOT NULL,
                "AgeGroup0_5" REAL,
                "AgeGroup5_10" REAL,
                "AgeGroup10_15" REAL,
                "AgeGroup15_20" REAL,
                "AgeGroup20_25" REAL,
                "AgeGroup25_30" REAL,
                "AgeGroup30_35" REAL,
                "AgeGroup35_40" REAL,
                "AgeGroup40_45" REAL,
                "AgeGroup45_50" REAL,
                "AgeGroup50_55" REAL,
                "AgeGroup55_60" REAL,
                "AgeGroup60_65" REAL,
                "AgeGroup65_70" REAL,
                "AgeGroup70_75" REAL,
                "AgeGroup75_80" REAL,
                "AgeGroup80_85" REAL,
                PRIMARY KEY ("CancerSite")
            )
        ''')

        # Insert data into the table, skipping the first dictionary
        for i in range(1, len(data)):
            cancer_data = data[i]
            cursor.execute(f'''
                INSERT INTO "{country}" (
                    "CancerSite",
                    "AgeGroup0_5",
                    "AgeGroup5_10",
                    "AgeGroup10_15",
                    "AgeGroup15_20",
                    "AgeGroup20_25",
                    "AgeGroup25_30",
                    "AgeGroup30_35",
                    "AgeGroup35_40",
                    "AgeGroup40_45",
                    "AgeGroup45_50",
                    "AgeGroup50_55",
                    "AgeGroup55_60",
                    "AgeGroup60_65",
                    "AgeGroup65_70",
                    "AgeGroup70_75",
                    "AgeGroup75_80",
                    "AgeGroup80_85"
                )
                VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
            ''', (
                cancer_data.get('CancerSite', ''),
                cancer_data.get('5', 0),
                cancer_data.get('10', 0),
                cancer_data.get('15', 0),
                cancer_data.get('20', 0),
                cancer_data.get('25', 0),
                cancer_data.get('30', 0),
                cancer_data.get('35', 0),
                cancer_data.get('40', 0),
                cancer_data.get('45', 0),
                cancer_data.get('50', 0),
                cancer_data.get('55', 0),
                cancer_data.get('60', 0),
                cancer_data.get('65', 0),
                cancer_data.get('70', 0),
                cancer_data.get('75', 0),
                cancer_data.get('80', 0),
                cancer_data.get('85', 0),
            ))

        # Commit the transaction
        conn.commit()

        return jsonify({"message": f"Table '{country}' created successfully"}), 200

    except Exception as e:
        # Handle exceptions
        return jsonify({"error": str(e)}), 500

    finally:
        # Close connection
        conn.close()

@app.route('/')
def index():
    germany_data = GERMANY.query.all()
    return render_template('index.html', germany_data=germany_data)

# Add this route to your Flask application
@app.route('/get_tables', methods=['GET'])
def get_tables():
    # Connect to SQLite database
    conn = sqlite3.connect('/root/dataviz/dataviz_project/db/database.db')
    cursor = conn.cursor()

    # Get the list of tables
    cursor.execute("SELECT name FROM sqlite_master WHERE type='table';")
    tables = cursor.fetchall()

    # Close the SQLite connection
    conn.close()

    # Return the list of tables as JSON
    return jsonify({"tables": [table[0] for table in tables]})



@app.route('/<string:country>')
def countries(country):
    use_alchemy = False
    if country == "germany" :
        data = GERMANY.query.all()
        use_alchemy = True

    elif country == "canada" :
        data = CANADA.query.all()
        use_alchemy = True

    elif country == "suiss" :
        data = SUIS.query.all()
        use_alchemy = True
    
    elif country == "usa":
        data = USA.query.all()
        use_alchemy = True
    
    else:
        # Connect to SQLite database
        conn = sqlite3.connect('/root/dataviz/dataviz_project/db/database.db')
        cursor = conn.cursor()  
        data = cursor.execute(f'''
            SELECT * FROM "{country}"
        ''').fetchall()  # Fetch the results
    
        # Close the SQLite connection
        conn.close()

        data_list = [
            {
                "CancerSite": entry[0],
                "5": entry[1],
                "10": entry[2],
                "15": entry[3],
                "20": entry[4],
                "25": entry[5],
                "30": entry[6],
                "35": entry[7],
                "40": entry[8],
                "45": entry[9],
                "50": entry[10],
                "55": entry[11],
                "60": entry[12],
                "65": entry[13],
                "70": entry[14],
                "75": entry[15],
                "80": entry[16],
                "85": entry[17],
            }
            for entry in data
        ]

    if use_alchemy:
        data_list = [
            {
                "CancerSite": entry.CancerSite,
                "5": entry.AgeGroup0_5,
                "10": entry.AgeGroup5_10,
                "15": entry.AgeGroup10_15,
                "20": entry.AgeGroup15_20,
                "25": entry.AgeGroup20_25,
                "30": entry.AgeGroup25_30,
                "35": entry.AgeGroup30_35,
                "40": entry.AgeGroup35_40,
                "45": entry.AgeGroup40_45,
                "50": entry.AgeGroup45_50,
                "55": entry.AgeGroup50_55,
                "60": entry.AgeGroup55_60,
                "65": entry.AgeGroup60_65,
                "70": entry.AgeGroup65_70,
                "75": entry.AgeGroup70_75,
                "80": entry.AgeGroup75_80,
                "85": entry.AgeGroup80_85,
                # Add other age groups as needed
            }
            for entry in data
        ]
    
    return data_list

if __name__ == '__main__':
    app.run(debug=True)