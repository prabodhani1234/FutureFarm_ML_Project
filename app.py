# Importing essential libraries and modules

from flask import Flask, render_template, request, Markup
import numpy as np
import pandas as pd
import requests
import config
import pickle
import io
from torchvision import transforms
from PIL import Image
from tensorflow.keras.models import load_model
from tensorflow.keras.preprocessing.image import load_img, img_to_array
from werkzeug.utils import secure_filename
import os, sys, glob, re


# ==============================================================================================

# ----------------------------- LOADING THE TRAINED MODELS -------------------------------------



# Loading soil classification model


model_path = "models/SoilImageCNN.h5"

SoilNet = load_model(model_path)
# model_path = "models/naive_bayes.joblib"
# SoilNet = joblib.load(model_path)


classes = {0:"Alluvial Soil",
1:"Black Soil",
2:"Clay Soil",
3:"Red Soil",
4:"Sandy Soil"}


def model_predict(image_path,model):
    print("Predicted")
    image = load_img(image_path,target_size=(256,256))
    image = img_to_array(image)
    image = image/255
    image = np.expand_dims(image,axis=0)
    
    result = np.argmax(model.predict(image))
    prediction = classes[result]
    
    
    if result == 0:
        print("Alluvial.html")
        
        return "Alluvial","Alluvial.html"
    elif result == 1:
        print("Black.html")
        
        return "Black", "Black.html"
    elif result == 2:
        print("Clay.html")
        
        return "Clay" , "Clay.html"
    elif result == 3:
        print("Red.html")
        
        return "Red" , "Red.html"

    elif result == 4:
        print("Sandy.html")
        
        return "Sandy" , "Sandy.html"
    

 
# Loading crop recommendation model

crop_recommendation_model_path = 'models/NBClassifier.pkl'
crop_recommendation_model = pickle.load(
    open(crop_recommendation_model_path, 'rb'))

    

# =========================================================================================

# Custom functions for calculations


def weather_fetch(city_name):
    """
    Fetch and returns the temperature and humidity of a city
    :params: city_name
    :return: temperature, humidity
    """
    api_key = config.weather_api_key
    base_url = "http://api.openweathermap.org/data/2.5/weather?"

    complete_url = base_url + "appid=" + api_key + "&q=" + city_name
    response = requests.get(complete_url)
    x = response.json()

    if x["cod"] != "404":
        y = x["main"]

        temperature = round((y["temp"] - 273.15), 2)
        humidity = y["humidity"]
        return temperature, humidity
    else:
        return None




# ===============================================================================================
# ------------------------------------ FLASK APP -------------------------------------------------


app = Flask(__name__)

# render home page


@ app.route('/')
def home():
    title = 'FutureFarm - Home'
    return render_template('index.html', title=title)


@ app.route('/about')
def about():
    title = 'FutureFarm - about'
    return render_template('about.html', title=title)
    
# render crop recommendation form page


@ app.route('/crop-recommend')
def crop_recommend():
    title = 'FutureFarm - Crop Recommendation'
    return render_template('crop.html', title=title)

# ===============================================================================================

# RENDER PREDICTION PAGES

# render Soil prediction input page

@app.route('/predict',methods=['GET','POST'])
def predict():
    print("Entered")
    if request.method == 'POST':
        print("Entered here")
        file = request.files['image'] # fet input
        filename = file.filename        
        print("@@ Input posted = ", filename)
        
        file_path = os.path.join('static/user uploaded', filename)
        file.save(file_path)

        print("@@ Predicting class......")
        pred, output_page = model_predict(file_path,SoilNet)
              
        return render_template(output_page, pred_output = pred, user_image = file_path)




# render crop recommendation result page


@ app.route('/crop-predict', methods=['POST'])
def crop_prediction():
    title = 'FutureFarm - Crop Recommendation'

    if request.method == 'POST':
        N = int(request.form['nitrogen'])
        P = int(request.form['phosphorous'])
        K = int(request.form['pottasium'])
        ph = float(request.form['ph'])
        temperature = float(request.form['temperature'])
        humidity = float(request.form['humidity'])
        rainfall = float(request.form['rainfall'])

        # state = request.form.get("stt")
        city = request.form.get("city")

        if weather_fetch(city) != None:
            data = np.array([[N, P, K, temperature, humidity, ph, rainfall]])
            my_prediction = crop_recommendation_model.predict(data)
            final_prediction = my_prediction[0]

            return render_template('crop-result.html', prediction=final_prediction, title=title)

        else:

            return render_template('try_again.html', title=title)




# ===============================================================================================
if __name__ == '__main__':
    app.run(debug=True)
