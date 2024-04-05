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

# Function to save user data to a CSV file
def save_user_data(name, email, mobile, unique_id, dob):
    user_data = pd.DataFrame({'Name': [name], 'Email': [email], 'Mobile': [mobile], 'Unique ID': [unique_id], 'DOB': [dob]})
    user_data.to_csv('user_data.csv', mode='a', index=False, header=not os.path.exists('user_data.csv'))

# Provide the path to your Firebase credentials JSON file
cred = credentials.Certificate("NEET_portal/neet-exam-portal-57ad1-51c5e39090df.json")
firebase_admin.initialize_app(cred)

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
def sign_up_with_email_and_password(email, mobile, unique_id, password, confirm_password, dob, return_secure_token=True):
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
            return data['email']
        else:
            st.warning(data)
    except Exception as e:
        st.warning(f'Signup failed: {e}')

# Login function
def login(email_or_unique_id, password):
    try:
        if '@' in email_or_unique_id:
            email = email_or_unique_id
            if not is_valid_email(email):
                st.warning("Invalid email address. Please enter a valid email.")
                return
            userinfo = sign_in_with_email_and_password(email, password)
        else:
            unique_id = email_or_unique_id
            # Implement the logic for unique ID login
            # For example:
            # userinfo = sign_in_with_unique_id(unique_id, password)
            pass
        
        if userinfo:
            st.session_state.username = userinfo.get('username', '')
            st.session_state.useremail = userinfo.get('email', '')
            st.session_state.signedout = True
            st.session_state.signout = True
        else:
            st.warning('Login failed. Incorrect email/unique ID or password.')
    except Exception as e:
        st.error(f'An error occurred during login: {e}')

# Logout function
def logout():
    st.session_state.signout = False
    st.session_state.signedout = False   
    st.session_state.username = ''
    st.session_state.useremail = ''

# Forgot password function
def forgot_password():
    email = st.text_input('Email')
    if st.button('Send Reset Link'):
        success, message = reset_password(email)
        if success:
            st.success("Password reset email sent successfully.")
        else:
            st.warning(f"Password reset failed: {message}") 

# Function to send verification email with OTP
def send_verification_email(email, otp):
    sender_email = "your_email@gmail.com"
    sender_password = "your_password"
    subject = "Verification Code for NEET Portal"
    message = f"Your OTP for NEET Portal registration is: {otp}"

    msg = MIMEMultipart()
    msg['From'] = sender_email
    msg['To'] = email
    msg['Subject'] = subject
    msg.attach(MIMEText(message, 'plain'))

    with smtplib.SMTP('smtp.gmail.com', 587) as server:
        server.starttls()
        server.login(sender_email, sender_password)
        server.send_message(msg)

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
        # Generate OTP
        otp = ''.join(random.choices(string.digits, k=6))
        # Send verification email
        send_verification_email(email, otp)
        st.success('Please check your email for the verification code.')
        
        # Add code to verify OTP and complete registration process
        # You can prompt the user to enter the OTP received in their email and verify it here
    
# Admin login UI
def admin_login():
    st.title('Admin Login')
    username = st.text_input('Username')
    password = st.text_input('Password', type='password')
    
    if username == 'admin' and password == 'adminpass':
        st.success('Login successful!')
        # Add code to display registered students' entries and manage them
    elif st.button('Login'):
        st.error('Invalid username or password. Please try again.')
        
# User registration and login UI
def app():
    st.title('Welcome to Chances of Qualifying NEET Examination Portal')
    
    # Initialize session state variables
    st.session_state.setdefault('username', '')
    st.session_state.setdefault('useremail', '')
    st.session_state.setdefault('signedout', False)
    st.session_state.setdefault('signout', False)

    if not st.session_state.signedout:
        choice = st.selectbox('Login/Register/Admin-Login', ['Login', 'Register', 'Admin-Login'])

        if choice == 'Register':
            registration()  # Call the registration function
            
        elif choice =='Admin-Login':
            admin_login()  #call the admin login function
            
        else:
            st.title('Login')
            email_or_unique_id = st.text_input('Email Address or Unique ID')
            password = st.text_input('Password', type='password')
            if st.button('Login'):
                login(email_or_unique_id, password)

    if st.session_state.signout:
        st.markdown('*Name* : ' + st.session_state.username)
        st.markdown('*Email id*: ' + st.session_state.useremail)
        st.button('Log out', on_click=logout)

    st.title('*Thank You...!*')


if __name__ == "__main__":
    app()
