import numpy as np
import pandas as pd
import datetime as dt
import sqlalchemy
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine, func

from flask import Flask, jsonify


#################################################
# Database Setup
#################################################
engine = create_engine("sqlite:///./Resources/hawaii.sqlite")

# reflect an existing database into a new model
Base = automap_base()
# reflect the tables
Base.prepare(engine, reflect=True)

# Save reference to the table
Measurement = Base.classes.measurement
Station = Base.classes.station

#################################################
# Flask Setup
#################################################
app = Flask(__name__)

#################################################
# Flask Routes
#################################################

@app.route("/")
def welcome():
    """List all available api routes."""
    return (
        f"Available Routes:<br/>"
        f"/api/v1.0/precipitation<br/>"
        f"/api/v1.0/stations<br/>"
        f"/api/v1.0/tobs<br/>"
        "/api/v1.0/{start}/{end}"
        )

@app.route("/api/v1.0/precipitation")
def precipitation():
    # Create our session (link) from Python to the DB
    session = Session(engine)
    # Calculate the date one year from the last date in data set.
    year_ago = dt.date(2017, 8, 23) - dt.timedelta(days=365)
    # Perform a query to retrieve the data and precipitation scores
    results = session.query(Measurement.date, Measurement.prcp).\
    filter(Measurement.date > year_ago).all()

    prec_dict = dict(results)
    session.close()
    return jsonify(prec_dict)

@app.route("/api/v1.0/stations")
def stations():
    #create session link from Python to the DB
    session = Session(engine)
    #Perform query to retrieve station data
    results = session.query(Station.name).all()
    all_stations = list(np.ravel(results))
    session.close()
    return jsonify(all_stations)

@app.route("/api/v1.0/tobs")
def tobs():
    #create session link from Python to the DB
    session = Session(engine)
    #Define date parameters
    year_ago = dt.date(2017, 8, 23) - dt.timedelta(days=365)
    #Perform query to retrieve temperature data
    results = session.query(Measurement.tobs).\
    filter(Measurement.date > year_ago).\
    filter(Measurement.station == 'USC00519281').all()

    active_station_data = list(np.ravel(results))
    session.close()
    return jsonify(active_station_data)

@app.route("/api/v1.0/<start>/<end>")
def start_end(start, end):
    #create session link from Python to the DB
    session = Session(engine)

    min_temp = func.min(Measurement.tobs)
    avg_temp = func.avg(Measurement.tobs)
    max_temp = func.max(Measurement.tobs)

    temperature_results = session.query(min_temp, avg_temp, max_temp).\
    filter(Measurement.date >= start).\
    filter(Measurement.date <= end).all()

    # temperature_results = list(np.ravel)

    session.close
    return jsonify(temperature_results)

if __name__ == '__main__':
    app.run(debug=True)
