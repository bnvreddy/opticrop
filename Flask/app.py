from flask import Flask, render_template, request
import pickle
import numpy as np

app = Flask(__name__)

with open('crop_model.pkl', 'rb') as file:
    model = pickle.load(file)

with open('scaler.pkl', 'rb') as file:
    scaler = pickle.load(file)

@app.route('/')
def home():
    return render_template('home.html')


@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/predict', methods=['GET', 'POST'])
def predict():
    if request.method == 'POST':
        try:
            N = float(request.form['nitrogen'])
            P = float(request.form['phosphorous'])
            K = float(request.form['potassium'])
            temperature = float(request.form['temperature'])
            humidity = float(request.form['humidity'])
            ph = float(request.form['ph'])
            rainfall = float(request.form['rainfall'])

            features = np.array([[N, P, K, temperature, humidity, ph, rainfall]])
            
            scaled_features = scaler.transform(features)
            

            prediction = model.predict(scaled_features)
            result = prediction[0]

            return render_template('predict.html', prediction_text=f'Recommended Crop for your conditions: {result}')
            
        except Exception as e:
            return render_template('predict.html', prediction_text=f'Error: Please enter valid numbers. ({e})')

    return render_template('predict.html')

if __name__ == "__main__":
    app.run(debug=True)