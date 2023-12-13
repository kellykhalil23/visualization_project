from flask import Flask, render_template
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



@app.route('/')
def index():
    germany_data = GERMANY.query.all()
    canada_data = CANADA.query.all()
    suis_data = SUIS.query.all()
    return render_template('index.html', germany_data=germany_data, canada_data=canada_data, suis_data=suis_data)



if __name__ == '__main__':
    app.run(debug=True)