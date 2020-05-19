
import numpy as np
import pandas as pd

import datetime as dt
import time

# Python SQL toolkit and Object Relational Mapper
import sqlalchemy
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine, func, inspect, desc, asc


# Import Flask
from flask import Flask, jsonify


#################################################
# Database Setup
#################################################

engine = create_engine("sqlite:///Resources/hawaii.sqlite")
Base = automap_base()
Base.prepare(engine, reflect=True)
Measurement = Base.classes.measurement
Station = Base.classes.station
session = Session(engine)



# Create an app, being sure to pass __name__
app = Flask(__name__)


# Define what to do when a user hits the index route

welcome_text = """
<html>
   <h2> Welcome to the home page for sqlalchemy Homework #10. </h2> \n
   <h3> Use <a href="http://localhost:5000/api/v1.0/precipitation">/api/v1.0/precipitation</a> to query for precipitation.</h3> \n
    <h3>Use <a href="http://localhost:5000/api/v1.0/stations">/api/v1.0/stations</a> to query for stations. </h3> \n
    <h3>Use <a href="http://localhost:5000/api/v1.0/tobs">/api/v1.0/tobs</a> to query for tempreture observations. </h3> \n
    <h3>Use '/api/v1.0/<start>' and/ '/api/v1.0<stop>' in the format: yyyy-mm-dd to obtain \n
    min, max and average tempreture from a start day with <start> only or <start> and <end> for a range. </h3> \n
    
</html>
"""


@app.route("/")
def index():
    print("Server received request for 'index' page...")
    return welcome_text

@app.route("/api/v1.0/precipitation/")
def precipitation():
    print("Server received request for 'precipitation' page...")
    
    # Perform a query to retrieve the data and precipitation scores
    prec_list = []
    results = session.query(Measurement.date, Measurement.prcp).filter(Measurement.date.like('2017%')).order_by(asc(Measurement.date))
    for row in results:
        prec_list.append(row)
        
    prec_df = pd.DataFrame(prec_list)
    prec_df = prec_df.set_index('date')
    prec_df = prec_df.sort_values(by=['date'])
    prec_df.replace(np.nan,0, inplace=True)
    prec_dict = prec_df.to_dict()
        
    return jsonify(prec_dict)

@app.route("/api/v1.0/stations/")
def stations():
    print("Server received request for 'stations' page...")
    station_list = []
    results = session.query(Measurement.station).distinct(Measurement.station)
    for row in results:
        station_list.append(row)
    
    station_df =pd.DataFrame(station_list)
    station_dict = station_df.to_dict()
    
    return jsonify(station_dict)

@app.route("/api/v1.0/tobs/")
def tobs():
    print("Server received request for 'tempreture observations' page...")
    return "Welcome to the tempreture observations page!"

@app.route("/api/v1.0/<start>/")
def start():
    print("Server received request for 'range start' page...")
    return "Welcome to the start range page!"

@app.route("/api/v1.0/<stop>/")
def stop():
    print("Server received request for 'range stop' page...")
    return "Welcome to the end range page!"



if __name__ == "__main__":
    app.run(debug=True)
