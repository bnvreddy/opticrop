from flask import Flask, render_template, request
import pickle
import numpy as np

app = Flask(__name__)

# Load the saved model and scaler
with open('crop_model.pkl', 'rb') as file:
    model = pickle.load(file)

with open('scaler.pkl', 'rb') as file:
    scaler = pickle.load(file)

# 1. Home Route
@app.route('/')
def home():
    return render_template('home.html')

# 2. About Route
@app.route('/about')
def about():
    return render_template('about.html')

# 3. Predict Route (Handles both displaying the form and the prediction logic)
@app.route('/predict', methods=['GET', 'POST'])
def predict():
    if request.method == 'POST':
        try:
            # Extract data from form using the exact 'name' attributes from predict.html
            N = float(request.form['nitrogen'])
            P = float(request.form['phosphorous'])
            K = float(request.form['potassium'])
            temperature = float(request.form['temperature'])
            humidity = float(request.form['humidity'])
            ph = float(request.form['ph'])
            rainfall = float(request.form['rainfall'])

            # Array must match the EXACT order the model was trained on
            features = np.array([[N, P, K, temperature, humidity, ph, rainfall]])
            
            # Scale the features
            scaled_features = scaler.transform(features)
            
            # Predict
            prediction = model.predict(scaled_features)
            result = prediction[0]
            
            # Send result back to the predict.html page
            return render_template('predict.html', prediction_text=f'Recommended Crop for your conditions: {result}')
            
        except Exception as e:
            return render_template('predict.html', prediction_text=f'Error: Please enter valid numbers. ({e})')

    # If it's a GET request, just show the empty form
    return render_template('predict.html')

if __name__ == "__main__":
    app.run(debug=True)