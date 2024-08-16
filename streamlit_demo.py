import streamlit as st
import pickle
import numpy as np
from datetime import datetime

# Load the encoding dictionaries and decision tree model from pickle files
with open("label_encodings.pkl", "rb") as f:
    encoding_dicts = pickle.load(f)

with open("decision_tree_model.pkl", "rb") as f:
    decision_tree_model = pickle.load(f)

# Extract individual encoding dictionaries
city_dict = encoding_dicts["City"]
state_dict = encoding_dicts["State"]
make_dict = encoding_dicts["Make"]
model_dict = encoding_dicts["Model"]

# Set the title of the Streamlit app
st.title("Car Price Prediction")

# Create input fields for City, State, Make, Model, Year, and Mileage
year = st.number_input(
    "Year", min_value=1900, max_value=datetime.now().year, value=2020
)
mileage = st.number_input("Mileage", min_value=0, value=10000)
city = st.selectbox("City", list(city_dict.keys()))
state = st.selectbox("State", list(state_dict.keys()))
make = st.selectbox("Make", list(make_dict.keys()))
model = st.selectbox("Model", list(model_dict.keys()))

# Output a prediction based on the inputs
if st.button("Predict"):
    # Calculate mileage_age_interaction
    current_year = datetime.now().year
    age = current_year - year
    mileage_age_interaction = mileage * age

    # Encode the inputs using the dictionaries
    encoded_city = city_dict[city]
    encoded_state = state_dict[state]
    encoded_make = make_dict[make]
    encoded_model = model_dict[model]

    # Create a feature array for the model
    features = np.array(
        [
            [
                year,
                mileage,
                encoded_city,
                encoded_state,
                encoded_make,
                encoded_model,
                mileage_age_interaction,
            ]
        ]
    )

    # Make a prediction using the decision tree model
    log_predicted_price = decision_tree_model.predict(features)

    # Convert the log of the predicted price back to the original price
    predicted_price = np.exp(log_predicted_price)

    # Display the predicted price
    st.write(
        f"The predicted price for {make} {model} in {city}, {state} is ${predicted_price[0]:,.2f}."
    )
