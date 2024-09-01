from flask import Flask, request, jsonify
import joblib

# Load the saved model using joblib
with open('best_decision_tree_model.joblib', 'rb') as model_file:
    model = joblib.load(model_file)

# Initialize Flask app
app = Flask(__name__)

# Define a route for the default URL, which loads the form
@app.route('/')
def home():
    return "Welcome to the Arrest Prediction API!"

# Define a route for predictions
@app.route('/predict', methods=['POST'])
def predict():
    # Get data from POST request
    data = request.get_json(force=True)
    
    # Extract features from the data and convert them to the required format
    features = [[data['Weapon Type'], data['Stop Resolution'], 
                 data['Subject Perceived Race'], data['Subject Perceived Gender'], 
                 data['Subject Age Group']]]
    
    # Predict using the loaded model
    prediction = model.predict(features)
    
    # Return prediction as JSON
    return jsonify({'prediction': int(prediction[0])})

if __name__ == '__main__':
    app.run(port=5000, debug=True)
