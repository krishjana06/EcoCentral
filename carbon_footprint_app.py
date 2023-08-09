import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load sample data (replace with your own data loading code)
data = pd.read_csv('carbon_footprint_data.csv')

def main():
     # Link external CSS file for additional styling
    with open("styles.css") as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)
    
    st.title('Carbon Footprint Tracker')

    st.write("Welcome to the Carbon Footprint Tracker app!")
    st.write("Use the settings on the sidebar to explore different data trends.")

    st.sidebar.header('Settings')
    time_period = st.sidebar.radio('Select Time Period', ['Daily', 'Weekly', 'Monthly', 'Yearly'])

    st.sidebar.write('---')

    st.sidebar.subheader('About')
    st.sidebar.info("This app helps you track your carbon footprint over time.")

    # Custom CSS to set the background color
    bg_color = "#b0e0e6"  # Powder Blue color
    st.sidebar.markdown(
        f"""
        <style>
        .sidebar .sidebar-content {{
            background-color: {bg_color};
        }}
        </style>
        """,
        unsafe_allow_html=True
    )

    # Filter data based on selected time period
    if time_period == 'Daily':
        selected_data = data[['Date', 'Daily_Carbon_Footprint']]
    elif time_period == 'Weekly':
        selected_data = data[['Date', 'Weekly_Carbon_Footprint']]
    elif time_period == 'Monthly':
        selected_data = data[['Date', 'Monthly_Carbon_Footprint']]
    else:
        selected_data = data[['Date', 'Yearly_Carbon_Footprint']]

    st.write(f"## {time_period} Carbon Footprint Trends")

    # Line chart
    plt.figure(figsize=(10, 6))
    sns.lineplot(x='Date', y=selected_data.columns[1], data=selected_data)
    plt.xticks(rotation=45)
    st.pyplot(plt)

    # Bar chart
    st.write(f"## {time_period} Carbon Footprint Distribution")
    plt.figure(figsize=(10, 6))
    sns.barplot(x='Date', y=selected_data.columns[1], data=selected_data)
    plt.xticks(rotation=45)
    st.pyplot(plt)

    st.write('---')

    # Emission factors (g CO2 per km) for different vehicle types
    EMISSION_FACTORS = {
        "Car": 120,
        "Bus": 80,
        "Bike": 0.0
    }
    # Calculate carbon footprint
    st.subheader("Calculate Carbon Footprint")
    distance = st.number_input("Enter distance (km):", value=10.0, step=1.0)
    vehicle_type = st.selectbox("Select vehicle type:", list(EMISSION_FACTORS.keys()))

    
    
    if vehicle_type in EMISSION_FACTORS:
        emission_factor = EMISSION_FACTORS[vehicle_type]
        carbon_emission = (emission_factor / 1000) * distance  # Convert g to kg
        st.write(f"Your carbon footprint for {distance} km with a {vehicle_type} is {carbon_emission:.2f} kg CO2.")
    else:
        st.write("Invalid vehicle type.")
    st.write('---')

    # Calculate and display total carbon footprint
    st.subheader("Summarize Total Carbon Footprint")

    # Get user input for each activity
    car_distance = st.number_input("Enter car distance (km):", value=0.0, step=1.0)
    bus_distance = st.number_input("Enter bus distance (km):", value=0.0, step=1.0)
    bike_distance = st.number_input("Enter bike distance (km):", value=0.0, step=1.0)

    # Calculate emissions for each activity
     
    car_emission = carbon_footprint_calculator(car_distance, "Car")
    bus_emission = carbon_footprint_calculator(bus_distance, "Bus")
    bike_emission = carbon_footprint_calculator(bike_distance, "Bike")

    # Calculate total carbon footprint
    total_emission = car_emission + bus_emission + bike_emission

    st.write("Total Carbon Footprint Summary:")
    st.write(f"Car Emissions: {car_emission:.2f} kg CO2")
    st.write(f"Bus Emissions: {bus_emission:.2f} kg CO2")
    st.write(f"Bike Emissions: {bike_emission:.2f} kg CO2")
    st.write(f"Total Emissions: {total_emission:.2f} kg CO2")

if __name__ == '__main__':
    main()