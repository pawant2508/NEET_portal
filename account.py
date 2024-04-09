import streamlit as st
import firebase_admin
from firebase_admin import credentials, firestore
from firebase_admin import auth
import re
import random
import string
from datetime import datetime, timedelta

# Path to the service account key JSON file
service_account_key_path = "neet-exam-portal-57ad1-4f5e95416ce8.json"


try:
    # Initialize Firebase app with the service account key
    cred = credentials.Certificate(service_account_key_path)
    firebase_admin.initialize_app(cred)
    db = firestore.client()
except ValueError as e:
    st.error(f"Failed to initialize Firebase: {e}")
    st.stop()

# Function to check if the user is an authorized admin
def is_authorized_admin(user_email):
    # Implement your logic to check if the user is an admin
    # For example, you can maintain a list of authorized admin emails
    # and check if the user's email is in that list
    authorized_admin_emails = ["admin1@example.com", "admin2@example.com"]
    return user_email in authorized_admin_emails

# Admin panel functionality
def admin_panel():
    st.title("Admin Dashboard")
    st.write("Welcome, Admin!")

    # Add some sample admin functionalities
    st.subheader("Manage Users")
    st.write("Here you can manage user accounts.")

    # Example of displaying Firestore data
    users_ref = db.collection("users")
    users = users_ref.get()
    if users:
        st.write("User List:")
        for user in users:
            user_data = user.to_dict()
            st.write(f"- {user.id}: {user_data}")

    # Add more admin functionalities as needed
    st.subheader("Manage Content")
    st.write("Here you can manage content.")

    # Example of a form to add new content
    st.subheader("Add New Content")
    content_title = st.text_input("Title")
    content_description = st.text_area("Description")
    if st.button("Add Content"):
        # Add logic to save content to Firestore
        st.success(f"Content '{content_title}' added successfully!")

    # Add more components and functionalities here

    # Add your admin panel functionality here

# Admin login function
def admin_login():
    st.title("Admin Login")
    username = st.text_input("Username")
    password = st.text_input("Password", type="password")
    
    if st.button("Login"):
        try:
            # Authenticate the admin user
            user = auth.get_user_by_email(username)
            if user.email_verified and user.email == username:
                # Check if the user is an authorized admin
                if is_authorized_admin(username):
                    st.success("Login successful!")
                    admin_panel()  # Show admin panel
                else:
                    st.error("Unauthorized access. You are not an admin.")
            else:
                st.error("Invalid username or password.")
        except auth.UserNotFoundError:
            st.error("User not found.")
        except Exception as e:
            st.error(f"An error occurred: {e}")


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
def sign_up_with_email_and_password(name, email, mobile, unique_id, password, confirm_password, dob, category, return_secure_token=True):
    try:
        if password != confirm_password:
            st.warning("Passwords do not match!")
            return

        if mobile and not is_valid_mobile(mobile):
            st.warning("Invalid mobile number. Please enter a 10-digit number.")
            return

        # Check if age is at least 15 years
        min_date = datetime.today() - timedelta(days=15*365)  # 15 years ago
        if dob > min_date.date():
            st.warning("You must be at least 15 years old to register.")
            return

        # Save user data to Firestore
        user_data = {
            "name": name,
            "Email": email,
            "Phone_Number": mobile,
            "Unique_ID": unique_id,
            "DoB": dob.strftime('%Y-%m-%d'),
            "Category": category
        }
        db.collection('users').document(email).set(user_data)

        # Return success message
        st.success("Registration successful!")
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
    
    # Set the range of dates to display the whole year
    max_date = datetime(datetime.today().year, 12, 31).date()
    min_date = datetime(datetime.today().year - 100, 1, 1).date()

    dob = st.date_input('Date of Birth', min_value=min_date, max_value=max_date)
    
    st.write(f"You must be at least 15 years old to register.")

    category_options = ['GEN', 'OBC', 'SC', 'ST', 'NT', 'EWS']
    category = st.selectbox('Category', category_options)
    
    if st.button('Register'):
        sign_up_with_email_and_password(name, email, mobile, unique_id, password, confirm_password, dob, category)

# User login function (not included for brevity)
def user_login():
    pass

# Admin login function (not included for brevity)
def admin_panel():
    pass

# Main app function
def app():
    st.title('Welcome to Chances of Qualifying NEET Examination Portal')
    
    # Initialize session state variables
    st.session_state.setdefault('username', '')
    st.session_state.setdefault('useremail', '')
    st.session_state.setdefault('signedout', False)
    st.session_state.setdefault('signout', False)

    if not st.session_state.signedout:
        choice = st.selectbox('Login/Register', ['Login', 'Register', 'Admin Login'])

        if choice == 'Register':
            registration()  # Call the registration function
            
        elif choice == 'Admin Login':
            admin_login()  # Call the admin login function
            
        elif choice == 'Login':
            user_login()  # Call the user login function

    if st.session_state.signout:
        st.markdown('*Name* : ' + st.session_state.username)
        st.markdown('*Email id*: ' + st.session_state.useremail)
        st.button('Log out')

    st.title('*Thank You...!*')

if __name__ == "__main__":
    app()
