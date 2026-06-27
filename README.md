# 🌾 OptiCrop: Smart Agricultural Production Optimization

OptiCrop is an advanced, data-driven software system designed to optimize agricultural production. By leveraging Machine Learning, the system analyzes key soil and environmental factors—such as Nitrogen (N), Phosphorus (P), Potassium (K), temperature, humidity, pH, and rainfall—to provide intelligent, tailored crop recommendations. 

This empowers farmers to make informed decisions that maximize yield, reduce resource waste, and promote sustainable farming practices.

## 🛠️ Tech Stack

*   **Backend & Web Framework:** Python, Flask
*   **Machine Learning:** Scikit-Learn (Logistic Regression, K-Means Clustering, Decision Tree )
*   **Data Manipulation:** Pandas, NumPy
*   **Data Visualization:** Matplotlib, Seaborn

## 📁 Project Structure

The project is neatly organized into three main sub-directories to separate the raw data, the machine learning pipeline, and the web deployment.

```text
OptiCrop/
│
├── requirements.txt              # Python dependencies for the project
│
├── Dataset/                      # Contains the raw data used for training
│   └── Crop_recommendation.csv   
│
├── Training/                     # Contains the complete ML pipeline
│   └── model_training.ipynb      # EDA, Clustering, Model Training & Export
│
└── Flask/                        # Contains the web application
    ├── app.py                    # Main Flask server script
    ├── crop_model.pkl            # Serialized Logistic Regression model
    ├── scaler.pkl                # Serialized Standard Scaler
    ├── static/
    |   └── style.css             # CSS files for the frontend UI
    |
    └── templates/                # HTML files for the frontend UI
        ├── index.html            # Home page
        ├── about.html            # About page
        └── predict.html          # Prediction form & results page
```

## ⚙️ Setup and Installation

Follow these steps to set up and run the OptiCrop project locally.

### Prerequisites
Make sure you have [Python](https://www.python.org/downloads/) (version 3.8 or higher) installed.

### Step 1: Navigate to the Project
Open your terminal or command prompt and navigate to the main `OptiCrop` folder.

### Step 2: Create a Virtual Environment (Recommended)
```bash
python -m venv .venv
```
Activate the virtual environment:

* **Windows:** `.venv\Scripts\activate`
* **macOS/Linux:** `source .venv/bin/activate`

### Step 3: Install Dependencies
Install the required Python packages using the provided `requirements.txt` file:
```bash
pip install -r requirements.txt
```

### Step 4: Model Training & Data Analysis (First time only)
Before the Flask app can make predictions, you need to generate the model files.
1. Navigate to the `Training/` folder and open `model_training.ipynb` in Jupyter Notebook.
2. This notebook contains the complete pipeline: 
   * Data visualization (Distplots)
   * Unsupervised learning (Elbow method with K-Means clustering)
   * Supervised learning (Training Logistic Regression, Decision Trees, and Random Forest)
3. Run all the cells in the notebook. At the end, it will generate two files: `crop_model.pkl` and `scaler.pkl`.
4. **Important:** Move/copy these two `.pkl` files from the `Training/` folder into the `Flask/` folder.

### Step 5: Run the Flask Application
Once the `.pkl` files are in the Flask folder, navigate to the `Flask` directory:
```bash
cd Flask
```
Start the application server:
```bash
python app.py
```
The server will start on `http://127.0.0.1:5000`. Open this URL in your web browser to interact with the app.

## 🌐 Application Workflow

1.  **Home Page (`/`):** Introduction to the OptiCrop system and its goals.
2.  **About Page (`/about`):** Detailed explanation of the ML methodology, data features, and how the system benefits researchers and farmers.
3.  **Find Your Crop (`/predict`):** A user-friendly form to input N, P, K, Temperature, Humidity, pH, and Rainfall. Upon clicking "Predict", the Logistic Regression model processes the scaled input and returns the optimal crop.

## 📝 Contents of `requirements.txt`
*(If you need to create this file, copy the text below)*
```text
flask
scikit-learn
pandas
numpy
matplotlib
seaborn
```

​
