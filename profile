import streamlit as st

def main():
    st.title("Profile Page")

    # Create input fields for user profile
    user_profile_picture = st.file_uploader("Profile Picture")
    user_username = st.text_input("Username")
    user_location = st.text_input("Location")
    user_email = st.text_input("Email")

    st.write("Please answer a few questions about carbon emissions:")
    with st.form(key='carbon_questions'):
        st.write("1. On a scale of 1 to 10, how concerned are you about carbon emissions?")
        carbon_concern = st.slider("Concern Level", 1, 10, 5)

        st.write("2. Do you actively take steps to reduce your carbon footprint?")
        reduce_carbon = st.checkbox("Yes, I do")

        st.form_submit_button("Submit")


if __name__ == "__main__":
    main()
