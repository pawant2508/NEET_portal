import streamlit as st
import firebase_admin
from firebase_admin import credentials
import json
import requests
import re
import random
import string
from datetime import datetime, timedelta
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import streamlit as st
import pandas as pd

# Initialize Firebase app
if not firebase_admin._apps:
    cred = credentials.Certificate("neet-exam-portal-57ad1-51c5e39090df.json")
    firebase_admin.initialize_app(cred)

db = firestore.client()

# Email validation function
def is_valid_email(email):
    email_regex = r'^[a-z0-9._%+-]+@[a-z0-9.-]+\.[a-z]{2,}$'
    return re.match(email_regex, email) is not None

# Password strength validation function
def is_strong_password(password):
    min_length = 8
    has_uppercase = any(char.isupper() for char in password)
    has_lowercase = any(char.islower() for char in password)
    has_digit = any(char.isdigit() for char in password)
    has_special = any(char in '!@#$%^&*()_+-=[]{}|;:,.<>?/~' for char in password)
    
    return (
        len(password) >= min_length and
        has_uppercase and
        has_lowercase and
        has_digit and
        has_special
    )

# Unique ID generation function
def generate_unique_id():
    characters = string.ascii_letters + string.digits + string.punctuation
    return ''.join(random.choice(characters) for _ in range(8))

# Mobile number validation function
def is_valid_mobile(mobile):
    return re.match(r'^\d{10}$', mobile) is not None

# Signup with email, password, username, category, mobile number, and date of birth
def sign_up_with_email_and_password(name, email, mobile, unique_id, password, confirm_password, dob, return_secure_token=True):
    try:
        if password != confirm_password:
            st.warning("Passwords do not match!")
            return

        if mobile and not is_valid_mobile(mobile):
            st.warning("Invalid mobile number. Please enter a 10-digit number.")
            return

        rest_api_url = "https://identitytoolkit.googleapis.com/v1/accounts:signUp"
        payload = {
            "email": email,
            "password": password,
            "returnSecureToken": return_secure_token
        }
        if mobile:
            payload["mobile"] = mobile
        if unique_id:
            payload["unique_id"] = unique_id
        if dob:
            payload["dob"] = dob
        payload = json.dumps(payload)
        r = requests.post(rest_api_url, params={"key": "AIzaSyApr-etDzcGcsVcmaw7R7rPxx3A09as7uw"}, data=payload)
        data = r.json()
        if 'email' in data:
            # Save user data to Firestore
            user_data = {
                "name": name,
                "email": email,
                "mobile": mobile,
                "unique_id": unique_id,
                "dob": dob
            }
            db.collection('users').document(email).set(user_data)
            return data['email']
        else:
            st.warning(data)
    except Exception as e:
        st.warning(f'Signup failed: {e}')

# Registration UI
def registration():
    st.title('Registration')
    name = st.text_input('Name')
    email = st.text_input('Email Address')
    mobile = st.text_input('Mobile Number')
    unique_id = st.text_input('Unique ID')
    password = st.text_input('Password', type='password')
    confirm_password = st.text_input('Confirm Password', type='password')
    
    min_date = datetime(1900, 1, 1)
    dob = st.date_input('Date of Birth', min_value=min_date)
    
    if st.button('Register'):
        sign_up_with_email_and_password(name, email, mobile, unique_id, password, confirm_password, dob)

# User registration and login UI
def app():
    st.title('Welcome to Chances of Qualifying NEET Examination Portal')
    
    # Initialize session state variables
    st.session_state.setdefault('username', '')
    st.session_state.setdefault('useremail', '')
    st.session_state.setdefault('signedout', False)
    st.session_state.setdefault('signout', False)

    if not st.session_state.signedout:
        choice = st.selectbox('Login/Register', ['Login', 'Register'])

        if choice == 'Register':
            registration()  # Call the registration function
            
        else:
            st.title('Login')
            # Implement login functionality
            pass

    if st.session_state.signout:
        st.markdown('*Name* : ' + st.session_state.username)
        st.markdown('*Email id*: ' + st.session_state.useremail)
        st.button('Log out')

    st.title('*Thank You...!*')

if __name__ == "__main__":
    app()
  st.title('*Thank You...!*')


if __name__ == "__main__":
    app()
