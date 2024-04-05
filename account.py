import streamlit as st # type: ignore
import firebase_admin # type: ignore
from firebase_admin import credentials # type: ignore
import json
import requests # type: ignore
import re

# Initialize Firebase app
if not firebase_admin._apps:
    cred = credentials.Certificate("F:/Dotnet/pyhton_proj/NEET_Portal/neet-exam-portal-57ad1-51c5e39090df.json")
    firebase_admin.initialize_app(cred)

# Email validation function
def is_valid_email(email):
    email_regex = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
    return re.match(email_regex, email) is not None

# Password strength validation function
def is_strong_password(password):
    # Define password strength criteria (example criteria)
    min_length = 8
    has_uppercase = any(char.isupper() for char in password)
    has_lowercase = any(char.islower() for char in password)
    has_digit = any(char.isdigit() for char in password)
    has_special = any(char in '!@#$%^&*()_+-=[]{}|;:,.<>?/~' for char in password)
    
    # Check if password meets all criteria
    return (
        len(password) >= min_length and
        has_uppercase and
        has_lowercase and
        has_digit and
        has_special
    )

# Username validation function
def is_valid_username(username):
    return re.match(r'^[a-zA-Z]+$', username) is not None

def sign_up_with_email_and_password(email, password, confirm_password, username=None, return_secure_token=True):
    try:
        if password != confirm_password:
            st.warning("Passwords do not match!")
            return

        rest_api_url = "https://identitytoolkit.googleapis.com/v1/accounts:signUp"
        payload = {
            "email": email,
            "password": password,
            "returnSecureToken": return_secure_token
        }
        if username:
            payload["displayName"] = username 
        payload = json.dumps(payload)
        r = requests.post(rest_api_url, params={"key": "AIzaSyApr-etDzcGcsVcmaw7R7rPxx3A09as7uw"}, data=payload)
        data = r.json()
        if 'email' in data:
            return data['email']
        else:
            st.warning(data)
    except Exception as e:
        st.warning(f'Signup failed: {e}')

def sign_in_with_email_and_password(email=None, password=None, return_secure_token=True):
    rest_api_url = "https://identitytoolkit.googleapis.com/v1/accounts:signInWithPassword"

    try:
        payload = {
            "returnSecureToken": return_secure_token
        }
        if email:
            payload["email"] = email
        if password:
            payload["password"] = password
        payload = json.dumps(payload)
        r = requests.post(rest_api_url, params={"key": "AIzaSyApr-etDzcGcsVcmaw7R7rPxx3A09as7uw"}, data=payload)
        data = r.json()
        if 'email' in data:
            user_info = {
                'email': data['email'],
                'username': data.get('displayName')
            }
            return user_info
        else:
            st.warning(data)
    except Exception as e:
        st.warning(f'Signin failed: {e}')

def reset_password(email):
    try:
        rest_api_url = "https://identitytoolkit.googleapis.com/v1/accounts:sendOobCode"
        payload = {
            "email": email,
            "requestType": "PASSWORD_RESET"
        }
        payload = json.dumps(payload)
        r = requests.post(rest_api_url, params={"key": "AIzaSyApr-etDzcGcsVcmaw7R7rPxx3A09as7uw"}, data=payload)
        if r.status_code == 200:
            return True, "Reset email Sent"
        else:
            error_message = r.json().get('error', {}).get('message')
            return False, error_message
    except Exception as e:
        return False, str(e)

def login():
    try:
        email = st.session_state.email_input
        password = st.session_state.password_input
        if not is_valid_email(email):
            st.warning("Invalid email address. Please enter a valid email.")
            return
        if not is_strong_password(password):
            st.warning("Password does not meet strength requirements. Password must be at least 8 characters long and contain at least one uppercase letter, one lowercase letter, one digit, and one special character.")
            return
        userinfo = sign_in_with_email_and_password(email, password)
        if userinfo:
            st.session_state.username = userinfo.get('username', '')
            st.session_state.useremail = userinfo.get('email', '')
            st.session_state.signedout = True
            st.session_state.signout = True    
    except: 
        st.warning('Login Failed')


def logout():
    st.session_state.signout = False
    st.session_state.signedout = False   
    st.session_state.username = ''
    st.session_state.useremail = ''

def forgot_password():
    email = st.text_input('Email')
    if st.button('Send Reset Link'):
        success, message = reset_password(email)
        if success:
            st.success("Password reset email sent successfully.")
        else:
            st.warning(f"Password reset failed: {message}") 

# UI
def app():
    st.title('Welcome to Chances of qualifying NEET Examination Portal')
    
    if not st.session_state.get('username'):
        st.session_state.username = ''
    if not st.session_state.get('useremail'):
        st.session_state.useremail = ''
    if not st.session_state.get('signedout'):
        st.session_state.signedout = False
    if not st.session_state.get('signout'):
        st.session_state.signout = False

    if not st.session_state.signedout:
        choice = st.selectbox('Login/Register', ['Login', 'Register'])
        email = st.text_input('Email Address')
        password = st.text_input('Password', type='password')
        st.session_state.email_input = email
        st.session_state.password_input = password

        if choice == 'Register':
            username = st.text_input("Enter your unique username")
            if st.button('Create my account'):
                if not is_valid_email(email):
                    st.warning("Invalid email address. Please enter a valid email.")
                elif not is_strong_password(password):
                    st.warning("Password does not meet strength requirements. Password must be at least 8 characters long and contain at least one uppercase letter, one lowercase letter, one digit, and one special character.")
                elif not is_valid_username(username):
                    st.warning("Username can only contain upper and lower case letters.")
                else:
                    user = sign_up_with_email_and_password(email=email, password=password, confirm_password=password, username=username)
                    if user:
                        st.success('Account created successfully!')
                        st.markdown('Please Login using your email and password')
                        st.balloons()
        else:
            st.button('Login', on_click=login)
            forgot_password()

    if st.session_state.signout:
        st.markdown('*Name* : ' + st.session_state.username)
        st.markdown('*Email id*: ' + st.session_state.useremail)
        st.button('Log out', on_click=logout)

    st.title('*Thank You...!*')

if __name__ == "_main_":
    app()
