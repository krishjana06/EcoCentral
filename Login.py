import streamlit as st

# Set page title and header
st.title("Eco Tracker - Login")

# Create a button for login
username = st.text_input("Username:")
password = st.text_input("Password:", type="password")
user_database = ["user1", "user2", "user3"]
password_database = ["rufus"]

if st.button("Log in"):
    if username in user_database:
        if password in password_database:
            st.success("Welcome, " + username + "!")
        else:
            st.error("Incorrect password. Please try again.")
    else:
        st.warning("User not found. Please sign up for an account.")

        st.button("Sign Up")
