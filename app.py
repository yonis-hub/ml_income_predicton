# Import libraries
import numpy as np
from flask import Flask, request, jsonify, render_template
import joblib
from pickle import load
import numpy as np
import random
import csv


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
  
    
    webpage = render_template("predictions_model.html",)
    return webpage


#this rought has the about team info
@app.route("/magic")
def magicHappenshere():
      #income prediction labels
    prediction_labels = ["Less than $50k","Greater than or equal $50K"]

    # Load the model.
    randomforest = load(open('static/data/randomforest.pkl', 'rb'))

    # Load the scaler.
    scaler = load(open('static/data/scaler.pkl', 'rb'))

    # add file here
    with open('static/data/dataset.csv') as f:
        reader = csv.reader(f)
        chosen_row = random.choice(list(reader))

        index_num = chosen_row[0]
        # print(index_num)

        chosen_row_float = [float(x) for x in chosen_row[1:] ]
        # print(chosen_row)

        chosen_row_reshape = [np.array(chosen_row_float)]
        # print(chosen_row_reshape)
        
        prediction_scaled = scaler.transform(chosen_row_reshape)
        # print(prediction_scaled)

        
        predict = randomforest.predict(prediction_scaled) 
        
        our_str = "Our Random Forest Model Predicts the Income to be: \n"
        modle_prediction = prediction_labels[predict[0]]
        index_str = (f' Test data is being pulled from Index: {index_num}')

        return (our_str + prediction_labels[predict[0]] + '.') + index_str 


#this rought has the about team info
@app.route("/team")
def aboutTeam():
    webpage = render_template("about_us.html")
    return webpage


#  flask requirment to run properly
if __name__ == '__main__':
    app.run(debug=True)