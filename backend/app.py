from flask import Flask, request, jsonify
import joblib
import pandas as pd
from flask_cors import CORS  # For enabling CORS support

# Initialize Flask app
app = Flask(__name__)
CORS(app)  # Enable CORS for all routes

# Load pre-trained model and preprocessing tools using joblib
preprocessor = joblib.load('../backend/preprocessor.joblib')
model = joblib.load('../backend/random_forest_model.joblib')
le = joblib.load('../backend/label_encoder.joblib')

@app.route('/predict', methods=['POST'])
def predict():
    try:
        # Get the JSON data from the request
        data = request.get_json()
        
        # Convert JSON data to DataFrame
        single_row_df = pd.DataFrame([data])
        
        # Drop unnecessary columns (if any)
        single_row_df.drop(['car_name', 'brand'], axis=1, errors='ignore', inplace=True)
        
        # Encode the 'model' column
        single_row_df['model'] = le.transform(single_row_df['model'])
        
        # Ensure column order matches training data
        original_columns = [
            'model', 'vehicle_age', 'km_driven', 'seller_type', 'fuel_type', 
            'transmission_type', 'mileage', 'engine', 'max_power', 'seats'
        ]
        single_row_df = single_row_df[original_columns]

        # Apply preprocessing
        single_row_transformed = preprocessor.transform(single_row_df)
        
        # Predict using the model
        predicted_price = model.predict(single_row_transformed)[0]
        
        # Calculate price range (-30k to +30k)
        lower_bound = max(0, predicted_price - 30000)
        upper_bound = predicted_price + 30000
        
        # Return prediction range and message
        return jsonify({
            'predicted_price': round(predicted_price, 2),
            'price_range': [round(lower_bound, 2), round(upper_bound, 2)],
            'message': (
                "The actual price can vary depending on the car's condition. "
                "A well-maintained car may be valued at the higher end, "
                "while a poorly maintained car might fall towards the lower end."
            )
        })
    
    except Exception as e:
        return jsonify({'error': str(e)})

if __name__ == '__main__':
    app.run(debug=True)
