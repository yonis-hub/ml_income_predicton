# Import libraries
import numpy as np
from flask import Flask, request, jsonify, render_template
import joblib
from pickle import load


# Placeholder code incase we use a db
# Define the database connection parameters
    # database_name = ''
    # connection_string = f'postgresql://{username}:{password}@localhost:5432/{database_name}'
# Connect to the database
# Import tables


# Instantiate the Flask application
app = Flask(__name__)
app.config['SEND_FILE_MAX_AGE_DEFAULT'] = 0 # Effectively disables page caching

#load scalers here




### Define app routes ###
# Index
@app.route("/")
def home():
    webpage = render_template("index.html")
    return webpage

@app.route("/about")
def aboutTeam():
    webpage = render_template("about.html")
    return webpage

# route that takes user input and makes a predictions
@app.route("/predict", medthods=['POST'])
def predictor():

    webpage = render_template("mlmodel.html" )
    return webpage



# This statement is required
# Final lines for Flask to run properly
if __name__ == '__main__':
    app.run(debug=True)