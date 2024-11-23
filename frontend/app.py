import streamlit as st
import requests

# Streamlit app title
st.set_page_config(page_title="Car Price Prediction", layout="wide")
st.title("Car Price Prediction")

# Sidebar for navigation
st.sidebar.title("Navigation")
section = st.sidebar.radio("Go to", ["Prediction", "About"])

if section == "Prediction":
    st.header("Car Price Prediction Form")
    # Prediction section content
    car_model = st.text_input("Car Model", "Swift")
    vehicle_age = st.number_input("Vehicle Age (in years)", min_value=0, max_value=50, step=1, value=5)
    km_driven = st.number_input("Kilometers Driven", min_value=0, step=1000, value=45000)
    seller_type = st.selectbox("Seller Type", ["Dealer", "Individual"])
    fuel_type = st.selectbox("Fuel Type", ["Petrol", "Diesel"])
    transmission_type = st.selectbox("Transmission Type", ["Manual", "Automatic"])
    mileage = st.number_input("Mileage (km/l)", min_value=0.0, value=20.4, step=0.1)
    engine = st.number_input("Engine Capacity (cc)", min_value=500, step=50, value=1200)
    max_power = st.number_input("Max Power (bhp)", min_value=30, step=10, value=82)
    seats = st.number_input("Number of Seats", min_value=2, max_value=10, step=1, value=5)

    # Submit button for prediction
    if st.button("Predict"):
        # Prepare the input data as JSON
        input_data = {
            "model": car_model,
            "vehicle_age": vehicle_age,
            "km_driven": km_driven,
            "seller_type": seller_type,
            "fuel_type": fuel_type,
            "transmission_type": transmission_type,
            "mileage": mileage,
            "engine": engine,
            "max_power": max_power,
            "seats": seats
        }

        # Make POST request to Flask backend
        response = requests.post(
            "http://127.0.0.1:5000/predict", 
            json=input_data
        )

        # Display the prediction
        if response.status_code == 200:
            result = response.json()
            if "predicted_price" in result:
                predicted_price = result['predicted_price']
                price_range = result['price_range']
                message = result['message']
                
                # Display the results with dynamic conditions
                st.success(f"Predicted Accurate Selling Price: ₹{predicted_price:,.2f}")
                st.write(
                    f"The **price range** for this car is estimated to be between "
                    f"₹{price_range[0]:,.2f} and ₹{price_range[1]:,.2f}."
                )
                
                # Additional condition-based message
                if predicted_price > 500000:
                    st.info(
                        f"This car is priced relatively higher. "
                        f"Ensure it's well-maintained or has premium features to justify the price."
                    )
                elif predicted_price > 300000:
                    st.info(
                        f"This car falls into a mid-range pricing category. "
                        f"Great for budget-conscious buyers who want value for money."
                    )
                else:
                    st.info(
                        f"This car is priced in the lower range. "
                        f"Make sure to check for potential maintenance issues or repairs."
                    )
                st.info(message)
            else:
                st.error(f"Error: {result.get('error', 'Unknown error')}")
        else:
            st.error("Failed to connect to backend!")

elif section == "About":
    # About section content
    st.header("About This Project")
    st.markdown("""
    This **Car Price Prediction** web application leverages a machine learning model to predict the selling price of used cars based on various features such as car model, age, kilometers driven, fuel type, and more. The application is built using a **Random Forest Regressor** model, which is trained on a dataset from **CarDekho** containing almost **15,000 records**. The dataset includes important features such as the car's **model**, **vehicle age**, **kilometers driven**, **fuel type**, **transmission type**, and more.

    #### Key Features:
    - **Dataset**: The dataset consists of almost 15,000 records from the CarDekho website, which were used to train the model. The data includes both categorical and numerical features that influence car prices.
    - **Machine Learning Model**: The primary model used is the **Random Forest Regressor**, which provides an impressive **94% accuracy**. Random Forest was chosen for its robustness in handling complex, non-linear data. In addition, a **K-Nearest Neighbors (KNN)** model was also tested, achieving a **90% accuracy**, but Random Forest was selected for better overall performance.
    - **Interactive Web Interface**: The project uses **Streamlit** for building a user-friendly, interactive interface. Users can input car details, and the model will predict the price range. The prediction is based on the trained model and includes a price range to account for variations in car condition.
    - **Flask Backend**: The backend is built using **Flask**, which handles the model inference and preprocessing. Flask serves the model and provides predictions when data is sent from the Streamlit frontend.
    - **Price Range Prediction**: The model not only predicts a single price but also provides a price range (±30k) to give users an idea of the variability in pricing, depending on factors like car condition.

    #### Deployment:
    - The application is deployed on **Render** for the backend (Flask API) and **Vercel** for hosting the frontend (Streamlit application).
    - These platforms provide a seamless and scalable environment to host web applications and APIs.

    ---
    <p style="text-align:center; font-size:20px; color:#FFD700;">
    Made by <a href="https://github.com/prince2004patel" style="color:#FFD700; text-decoration:none;"><b>Prince Patel</b></a>
    </p>
    """, unsafe_allow_html=True)
