import streamlit as st
import pyodbc
import re
import random
import string
from datetime import datetime, timedelta

# Database connection configuration
server = 'DESKTOP-3CL2OGS\SQLEXPRESS'  # Assuming SQL Server is running locally
database = 'NeetRegistrationDB'

# Connect to SQL Server
try:
    conn = pyodbc.connect(f'DRIVER={{SQL Server}};SERVER={server};DATABASE={database}')
    cursor = conn.cursor()
except pyodbc.Error as e:
    st.error(f"Failed to connect to SQL Server: {e}")
    st.stop()


# Admin panel functionality
def admin_panel():
    st.title("Admin Dashboard")
    st.write("Welcome, Admin!")

    # Add some sample admin functionalities
    st.subheader("Manage Users")
    st.write("Here you can manage user accounts.")

    # Example of displaying user data from the database
    cursor.execute("SELECT * FROM Users")
    users = cursor.fetchall()
    if users:
        st.write("User List:")
        for user in users:
            st.write(user)

    # Add more admin functionalities as needed

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
def sign_up_with_email_and_password(name, email, mobile, unique_id, password, confirm_password, dob, category):
    try:
        if password != confirm_password:
            st.warning("Passwords do not match!")
            return

        # Check if age is at least 15 years
        min_date = datetime.today() - timedelta(days=15*365)  # 15 years ago
        if dob > min_date.date():
            st.warning("You must be at least 15 years old to register.")
            return

        # Save user data to the database
        cursor.execute("INSERT INTO Users (FullName, Email, MobileNo, UniqueID, Passwords, DoB, Category) VALUES (?, ?, ?, ?, ?, ?, ?)",
                       (name, email, mobile, unique_id, password, dob.strftime('%Y-%m-%d'), category))
        conn.commit()

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

# User login function
def login_page(email, uniqueID, password):
    st.title("User Login")
    
    email_UniqueID = st.text_input('Email/Unique ID')
    password = st.text_input('Password', type='password')
    try:
        # Query the Users table to check if the provided email/uniqueID and password are valid
        cursor.execute("SELECT * FROM Users WHERE (Email = ? OR UniqueID = ?) AND Passwords = ?", (email, uniqueID, password))
        user = cursor.fetchone()
        
        if user:
            # Successfully logged in
            st.write("Login successful!")
            # You can also return user information or perform additional actions here
            return True
        else:
            # Invalid credentials
            st.write("Invalid email/uniqueID or password.")
            return False
            
    except pyodbc.Error as e:
        # Error occurred during SQL query execution
        st.error(f"An error occurred while executing the SQL query: {e}")
        return False

# Admin login function (not included for brevity)
def admin_login(username, password):
    try:
        # Query the admin table to check if the provided credentials are valid
        cursor.execute("SELECT * FROM Admins WHERE Username = ? AND Password = ?", (username, password))
        admin = cursor.fetchone()
        if admin:
            st.success('Login successful!')
            return True
        else:
            st.error('Invalid email, username, or password')
            return False
    except pyodbc.Error as e:
        st.error(f"An error occurred while executing the SQL query: {e}")
        return False
    
# Admin dashboard function
def admin_dashboard():
    st.title('Admin Dashboard')
    # Add administrative functionalities here

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
                st.title('Admin Panel')
                if not st.session_state.get('logged_in'):
                    username = st.text_input('Username')
                    password = st.text_input('Password', type='password')
                    if st.button('Login'):
                        if admin_login(username, password):
                            st.session_state.logged_in = True
                            admin_dashboard()
                        else:
                            admin_dashboard()
                            
        elif choice == 'Login':
            login_page()  # Call the user login function

    if st.session_state.signout:
        st.markdown('*Name* : ' + st.session_state.username)
        st.markdown('*Email id*: ' + st.session_state.useremail)
        st.button('Log out')

    st.title('*Thank You...!*')

if __name__ == "__main__":
    app()
