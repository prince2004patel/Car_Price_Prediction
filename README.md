# First End-to-End Car Price Prediction Web App Using Machine Learning

This project is a web application that predicts the price of a car based on features such as car model, vehicle age, mileage, and more. It uses machine learning to provide accurate car price predictions. The backend is powered by Flask, and the frontend uses Streamlit for an interactive user experience.

## Live Deployment Link

- **Car Price Prediction Web App**: <a href="https://car-price-prediction-frontend.onrender.com" target="_blank">Click here to visit the app</a>

## Key Features

- **Machine Learning Model**: Uses Random Forest to predict car prices with an accuracy of **92%**.
- **Backend**: Flask to handle prediction requests.
- **Frontend**: Streamlit web app for easy user interaction.
- **Deployment**: Both backend and frontend deployed on Render.

## Technologies Used

- **Backend**: Flask (Python web framework)
- **Frontend**: Streamlit (for building the interactive web app)
- **Machine Learning**: Random Forest (for price prediction)
- **Deployment**: Render (for deploying both frontend and backend)
- **Data Processing**: 
  - **scikit-learn** (for model training and preprocessing)
  - **joblib** (for model serialization)
  - **numpy** (for numerical operations)
  - **pandas** (for data manipulation and analysis)
  - **matplotlib** (for data visualization)
  - **seaborn** (for statistical data visualization)
  - **flask_cors** (for enabling CORS support in the Flask API)
    
## Machine Learning Model

### Model: Random Forest

The car price prediction model uses the **Random Forest** algorithm, an ensemble learning method. It has been trained on a dataset with car attributes such as:
- Car Model
- Vehicle Age
- Kilometers Driven
- Seller Type
- Fuel Type
- Transmission Type
- Mileage
- Engine Power
- Seats

**Model Accuracy**:  
The car price prediction model achieves **92% accuracy** using Random Forest, which is highly reliable for real-world applications. While a K-Nearest Neighbors (KNN) model was also considered, it provided a slightly lower accuracy of **90%**. However, the Random Forest model, although more accurate, results in a larger joblib file size, which posed challenges for deployment on Render. To ensure efficient deployment without compromising model performance, optimizations were made to reduce the model size while maintaining high prediction accuracy.

---

Thank you for checking out this project!
