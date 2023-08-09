import streamlit as st
import pandas as pd

# Set page title and header
st.title("Eco Tracker - Carbon Footprint Calculator")
st.header("Enter Your Car Usage Information")

# Initialize session state variables
if "csv_exists" not in st.session_state:
    st.session_state.csv_exists = False

# Collect user information
hours_per_day = st.number_input("Approximate hours you drive a car each day:", min_value=0.0, step=0.1)
hours_per_week = st.number_input("Approximate hours you drive a car each week:", min_value=0.0, step=0.1)
hours_per_month = st.number_input("Approximate hours you drive a car each month:", min_value=0.0, step=0.1)
hours_per_year = st.number_input("Approximate hours you drive a car each year:", min_value=0.0, step=0.1)

# Create a dictionary to store user information
user_data = {
    "Hours per Day": hours_per_day,
    "Hours per Week": hours_per_week,
    "Hours per Month": hours_per_month,
    "Hours per Year": hours_per_year
}

# Create a DataFrame from the user data
user_df = pd.DataFrame([user_data])

# Save user data to a CSV file
if st.button("Submit"):
    user_df.to_csv("user_data.csv", mode="a", header=not st.session_state.csv_exists, index=False)
    st.success("Data saved successfully!")
    st.session_state.csv_exists = True

# Apply Eco theme styling
eco_css = """
<style>
body {
    background-color: #3C9C41;
    color: white;
}
header {
    color: #43B02A;
}
</style>
"""
st.markdown(eco_css, unsafe_allow_html=True)
