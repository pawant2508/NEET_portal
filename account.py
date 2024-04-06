import streamlit as st
import firebase_admin
from firebase_admin import credentials, firestore
import json
import requests
import re
import random
import string
from datetime import datetime, timedelta
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

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

# Send verification email with OTP
def send_verification_email(email, otp):
    sender_email = "your_service_email@gmail.com"
    sender_password = "your_service_email_password"
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

# Signup with email, password, username, category, mobile number, and date of birth
def sign_up_with_email_and_password(name, email, mobile, unique_id, password, confirm_password, dob, category, otp, return_secure_token=True):
    try:
        if password != confirm_password:
            st.warning("Passwords do not match!")
            return

        if mobile and not is_valid_mobile(mobile):
            st.warning("Invalid mobile number. Please enter a 10-digit number.")
            return

        # Check if age is at least 15 years
        today = datetime.today()
        min_date = today - timedelta(days=15*365)  # 15 years ago
        if dob > min_date:
            st.warning("You must be at least 15 years old to register.")
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
            payload["dob"] = dob.strftime('%Y-%m-%d')
        if category:
            payload["category"] = category
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
                "dob": dob.strftime('%Y-%m-%d'),
                "category": category
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
    
    dob = st.date_input('Date of Birth')

    today = datetime.today()
    min_date = today - timedelta(days=15*365)  # 15 years ago
    st.write(f"You must be at least 15 years old to register. Minimum date of birth: {min_date.strftime('%Y-%m-%d')}")

    if dob > min_date:
        st.warning("You must be at least 15 years old to register.")
        return

    category_options = ['GEN', 'OBC', 'SC', 'ST', 'NT', 'EWS']
    category = st.selectbox('Category', category_options)
    
    # Generate OTP
    otp = ''.join(random.choices(string.digits, k=6))
    st.text('An OTP has been sent to your email address. Please enter it below.')
    
    if st.button('Register'):
        sign_up_with_email_and_password(name, email, mobile, unique_id, password, confirm_password, dob, category, otp)
        send_verification_email(email, otp)  # Send verification email

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
