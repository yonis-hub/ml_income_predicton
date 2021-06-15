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
#main/home page this will have our ml model analysis
@app.route("/")
def home():
    webpage = render_template("index.html")
    return webpage

#this rought explains where and what dataset we are using for our ml models
@app.route("/about")
def projectOverview():
    webpage = render_template("about.html")
    return webpage

# We might have to move away from making any predcitons 
# might delete this route
# route that takes user input and makes a predictions
@app.route("/predictor")
def predictor():
    webpage = render_template("predictions_model.html" )
    return webpage

#this rought has the about team info
@app.route("/team")
def aboutTeam():
    webpage = render_template("about_us.html")
    return webpage


#  flask requirment to run properly
if __name__ == '__main__':
    app.run(debug=True)