# Import Flask
from flask import Flask

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
    return "Welcome to precipitation page "

@app.route("/api/v1.0/stations/")
def stations():
    print("Server received request for 'stations' page...")
    return "Welcome to my 'About' page!"

@app.route("/api/v1.0/tobs/")
def tobs():
    print("Server received request for 'tempreture observations' page...")
    return "Welcome to my 'About' page!"

@app.route("/api/v1.0/<start>/")
def start():
    print("Server received request for 'range start' page...")
    return "Welcome to my 'About' page!"

@app.route("/api/v1.0/<stop>/")
def stop():
    print("Server received request for 'range stop' page...")
    return "Welcome to my 'About' page!"



if __name__ == "__main__":
    app.run(debug=True)
