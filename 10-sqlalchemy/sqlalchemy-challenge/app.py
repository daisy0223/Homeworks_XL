# 1. Import dependences
import numpy as np
import sqlalchemy
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine, func
import datetime as dt
from flask import Flask, jsonify
# Database Setup
engine = create_engine("sqlite:///hawaii.sqlite")
# reflect an existing database into a new model
Base = automap_base()
# reflect the tables
Base.prepare(engine, reflect=True)

# Save reference to the table
Measurement = Base.classes.measurement
Station = Base.classes.station

# Query the end date and one year before that
session = Session(engine)
latest_date=session.query(Measurement.date).order_by(Measurement.date.desc()).first()
query_date = dt.date(2017, 8, 23) - dt.timedelta(days=365)
session.close()

# 2. Create an app
app = Flask(__name__)

# 3. Define static routes
@app.route("/")
def index():
    return (
        f"Welcome to the Homepage!<br/>"
        f"Available Routes:<br/>"
        f"Precipitation: /api/v1.0/precipitation<br/>"
        f"Station list: /api/v1.0/stations<br/>"
        f"One-year temperature: /api/v1.0/tobs<br/>"
        f"Temperature search using only start date(yyyy-mm-dd): /api/v1.0/yyyy-mm-dd<br/>"
        f"Temperature search using both start and end dates(yyyy-mm-dd): /api/v1.0/yyyy-mm-dd/yyyy-mm-dd"
    )

@app.route("/api/v1.0/precipitation")
def precipitation():
    session = Session(engine)
    result=session.query(Measurement.prcp, Measurement.date).filter(Measurement.date >= query_date).all()
    session.close()
    pre = []
    for date, prcp in result:
        pre_dict = {}
        pre_dict["prcp"] = prcp
        pre_dict["date"] = date
        pre.append(pre_dict)
    return jsonify(pre)
   
@app.route("/api/v1.0/stations")
def stations():
    session = Session(engine)
    station_query = session.query(Station.station).all()
    session.close()
    station_list=list(np.ravel(station_query))
    return jsonify(station_list)

@app.route("/api/v1.0/tobs")
def tobs():
    tob_query = session.query(Measurement.tobs).\
        filter(Measurement.date>query_date).\
        filter(Measurement.station=='USC00519281').all()
    tob_list=list(np.ravel(tob_query))
    return jsonify(tob_list)

@app.route("/api/v1.0/<start>")
def start(start):
    # take a date and format to yyyy-mm-dd
    start_date = dt.datetime.strptime(start, '%Y-%m-%d')
    # given the start only, calculate `TMIN`, `TAVG`, and `TMAX` for all dates greater than and equal to the start date.
    session = Session(engine)
    temp=session.query(func.min(Measurement.tobs),func.avg(Measurement.tobs),func.max(Measurement.tobs)).\
        filter(Measurement.date >= start_date).all()
    
    for TMIN, TAVG, TMAX in temp:
        temp_dict = {}
        temp_dict["TMIN"] = temp[0][0]
        temp_dict["TAVG"] = temp[0][1]
        temp_dict["TMAX"] = temp[0][2]

    return jsonify(temp_dict)
    session.close()

@app.route("/api/v1.0/<start>/<end>")
def both(start, end):
    # take start and end date and format to yyyy-mm-dd
    start_date = dt.datetime.strptime(start, '%Y-%m-%d')
    end_date = dt.datetime.strptime(end, '%Y-%m-%d')
    # Get TMIN`, `TAVG`, and `TMAX` for dates between the start and end date inclusive
    session = Session(engine)
    temp_both=session.query(func.min(Measurement.tobs),func.avg(Measurement.tobs),func.max(Measurement.tobs)).\
        filter(Measurement.date >= start_date).\
        filter(Measurement.date <= end_date).all()
    temp_list = list(np.ravel(temp_both))
    return jsonify(temp_list)
    session.close()
    
# 4. Define main behavior
if __name__ == "__main__":
    app.run(debug=True)