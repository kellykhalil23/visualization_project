from flask import Flask, render_template, jsonify
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

# Configure the SQLite database URI. Change the database URL as needed.
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:////root/dataviz/dataviz_project/db/database.db'
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

@app.route('/')
def index():
    germany_data = GERMANY.query.all()
    return render_template('index.html', germany_data=germany_data)

@app.route('/heatmaps')
def heatmaps():
    return render_template('heatmaps.html')


@app.route('/<string:country>')
def countries(country):
    if country == "germany" :
        data = GERMANY.query.all()

    elif country == "canada" :
        data = CANADA.query.all()

    elif country == "suiss" :
        data = SUIS.query.all()
    
    elif country == "usa":
        data = USA.query.all()
    
    
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