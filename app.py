
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

def calc_temps(start_date, end_date):
    """TMIN, TAVG, and TMAX for a list of dates.
    
    Args:
        start_date (string): A date string in the format %Y-%m-%d
        end_date (string): A date string in the format %Y-%m-%d
        
    Returns:
        TMIN, TAVE, and TMAX
    """
    
    return session.query(func.min(Measurement.tobs), func.avg(Measurement.tobs), func.max(Measurement.tobs)).\
        filter(Measurement.date >= start_date).filter(Measurement.date <= end_date).all()



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
<<<<<<< HEAD
   <h3> Use <a href="http://localhost:5000/api/v1.0/stations">/api/v1.0/stations</a> to query for stations. </h3> \n
   <h3> Use <a href="http://localhost:5000/api/v1.0/tobs">/api/v1.0/tobs</a> to query for tempreture observations. </h3> \n
   <h3> Use <a href="http://localhost:5000/api/v1.0/start">/api/v1.0/start</a> to query the tempreture min, average, and max for the entire dataset before 2017. </h3> \n
   <h3> Use <a href="http://localhost:5000/api/v1.0/start_end">/api/v1.0/start_end</a> to query the tempreture min, average, and max for the last year (2017) of the dataset. </h3>
=======
    <h3>Use <a href="http://localhost:5000/api/v1.0/stations">/api/v1.0/stations</a> to query for stations. </h3> \n
    <h3>Use <a href="http://localhost:5000/api/v1.0/tobs">/api/v1.0/tobs</a> to query for tempreture observations. </h3> \n
    <h3>Use <a href="http://localhost:5000/api/v1.0/start">api/v1.0/start</a> to query from date forward. </h3> \n
    min, max and average tempreture from a start day with <start> only or <start> and <end> for a range. </h3> \n
>>>>>>> d6a69ad8041408c9de7bbacfff0976aa1ae5be08
    
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
<<<<<<< HEAD
    temp_list = []
    results = session.query(Measurement.date, Measurement.tobs).filter(Measurement.date.like('2017%')).filter(Measurement.station.like('USC00519281')).order_by(asc(Measurement.date))
    for row in results:
        temp_list.append(row)
        
    temp_df = pd.DataFrame(temp_list)
    temp_dict = temp_df.to_dict()
    
    return jsonify(temp_dict)
=======
    tobs_list = []
    results = session.query(Measurement.date, Measurement.tobs).filter(Measurement.date.like('2017%')).filter(Measurement.station.like('USC00519281')).order_by(asc(Measurement.date))
    for row in results:
        tobs_list.append(row)
    
    tobs_df =pd.DataFrame(tobs_list)
    tobs_dict = tobs_df.to_dict() 
    
    return jsonify(tobs_dict)
>>>>>>> d6a69ad8041408c9de7bbacfff0976aa1ae5be08

@app.route("/api/v1.0/start/")
def start():
    print("Server received request for 'range start' page...")
    values = calc_temps('2010-01-01', '2016-12-31')
    key =['Pre_2017_Temp_Stats']
    pre_dict = dict(zip(key,values))
    return jsonify(pre_dict)

@app.route("/api/v1.0/start_end/")
<<<<<<< HEAD
def stop():
=======
def start_end():
>>>>>>> d6a69ad8041408c9de7bbacfff0976aa1ae5be08
    print("Server received request for 'range stop' page...")
    values = calc_temps('2017-01-01', '2017-08-30')
    key =['2017_Temp_Status']
    latest_dict = dict(zip(key,values))
    return jsonify(latest_dict)



if __name__ == "__main__":
    app.run(debug=True)
