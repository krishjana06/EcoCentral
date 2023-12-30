import streamlit as st
import pandas as pd

# Load sample data (replace with your own data loading code)
data = pd.read_csv('carbon_footprint_data.csv')

# Convert the 'Date' column to a datetime type
data['Date'] = pd.to_datetime(data['Date'])

def main():
    st.title("EcoCentral")
    st.subheader("A Carbon footprint helper! Help save the environment one step at a time.")
    # Carbon Footprint Calculator Section
    st.header("Carbon Footprint Calculator")

    # ... (Your existing code for the calculator)
    # Section for daily activities
    st.header("Electricity Usage")
    electricity_usage = st.slider("Average Monthly Electricity Usage (kWh - listed in the Electricty Bill)", 0.0, 10000.0, 0.0)

    st.header("Gas Consumption")
    gas_consumption = st.slider("Average Monthly Gas Consumption (Gallons)", 0.0, 2000.0, 0.0)

    # Section for transportation choices
    st.header("Transportation Choices")
    car_miles = st.slider("Miles Driven by Car per Month", 0.0, 7500.0, 0.0)
    flight_hours = st.slider("Monthly Flight Hours", 0.0, 250.0, 0.0)
    commuting_distance = st.slider("Daily Commuting Distance (miles)", 0.0, 500.0, 0.0)

    # Number of family members and explanation
    st.header("Number of Family Members")
    num_family_members = st.slider("Number of Family Members", 1, 10, 1)
    st.write(f"You have {num_family_members} family member(s). More family members can contribute to higher carbon emissions.")

    # Calculate button
    if st.button("Calculate Carbon Footprint"):
        # Define emission factors for each activity and mode of transportation
        electricity_emission_factor = 0.45  # kg CO2 per kWh
        gas_emission_factor = 2.0  # kg CO2 per cubic meter
        car_emission_factor = 0.2  # kg CO2 per mile
        flight_emission_factor = 200.0  # kg CO2 per hour
        commuting_emission_factor = 0.1  # kg CO2 per mile

        # Calculate carbon footprint based on user input
        total_emissions = (
            electricity_usage * electricity_emission_factor +
            gas_consumption * gas_emission_factor +
            car_miles * car_emission_factor +
            flight_hours * flight_emission_factor +
            commuting_distance * commuting_emission_factor
        )

        # Consider the number of family members in the calculation
        total_emissions_per_person = total_emissions / num_family_members

        # Display the result
        st.subheader("Your Carbon Footprint")
        st.write(f"Total Emissions: {total_emissions:.2f} kg CO2")
        st.write(f"Emissions Per Person: {total_emissions_per_person:.2f} kg CO2 per person")

        # Set a recommended maximum carbon footprint
        recommended_max_emissions = 10.0  # Replace with your recommended value

        # Compare the calculated emissions with the recommended maximum
        if total_emissions_per_person <= recommended_max_emissions:
            st.write("Your carbon footprint is within the recommended range. Great job!")
        else:
            st.write("Your carbon footprint is higher than the recommended range. Here are some suggestions to reduce it:")

            if total_emissions > recommended_max_emissions * 1.2:
                st.write("- Consider reducing car usage and using public transportation or carpooling.")
                st.write("- Reduce energy consumption by using energy-efficient appliances and turning off lights when not in use.")
            else:
                st.write("- Reduce car usage by walking or biking for short distances.")
                st.write("- Opt for flights with fewer layovers or consider alternatives like train or bus travel.")

    # Carbon Footprint Tracker Section
    # ... (Your existing code for the tracker)
    st.title('Carbon Footprint Tracker')
    
    st.sidebar.header('Graph Data and Trends')
    time_period = st.sidebar.radio('Select Time Period', ['Daily', 'Weekly', 'Monthly', 'Yearly'])

    st.sidebar.write('---')

    st.write(f"## {time_period} Carbon Footprint Trends")

    # Data collection
    user_data = {'Date': [], 'Daily_Carbon_Footprint': [], 'Weekly_Carbon_Footprint': [], 'Monthly_Carbon_Footprint': [], 'Yearly_Carbon_Footprint': []}

    
    date = st.date_input("Select Date", pd.to_datetime("today"))
    daily_carbon = st.number_input("Daily Carbon Footprint", value=0.0)
    weekly_carbon = st.number_input("Weekly Carbon Footprint", value=0.0)
    monthly_carbon = st.number_input("Monthly Carbon Footprint", value=0.0)
    yearly_carbon = st.number_input("Yearly Carbon Footprint", value=0.0)

    user_data['Date'].append(date)
    user_data['Daily_Carbon_Footprint'].append(daily_carbon)
    user_data['Weekly_Carbon_Footprint'].append(weekly_carbon)
    user_data['Monthly_Carbon_Footprint'].append(monthly_carbon)
    user_data['Yearly_Carbon_Footprint'].append(yearly_carbon)

    # Display entered data
    user_df = pd.DataFrame(user_data)
    st.write("Entered Data:")
    st.write(user_df)

    # Save data to CSV
    if st.button("Get CSV File"):
        user_df.to_csv('user_data.csv', index=False)
        st.success("CSV file saved successfully!")

    # Upload CSV File
    uploaded_file = st.file_uploader("Upload CSV File", type=["csv"])

    if uploaded_file is not None:
        uploaded_data = pd.read_csv(uploaded_file)
        st.write("Uploaded Data:")
        st.write(uploaded_data)

        # Visualization using uploaded data
        if not uploaded_data.empty:
            data_to_plot = uploaded_data

            # Display line chart
            st.line_chart(data_to_plot.set_index('Date')[time_period + '_Carbon_Footprint'])

if __name__ == '__main__':
    main()
