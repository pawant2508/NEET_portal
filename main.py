import streamlit as st # type: ignore
from firebase_option_menu import option_menu # type: ignore
import home, account, mock, mock_test_1, mock_test_2, mock_test_3, mock_test_4, mock_test_5, mock_test_6, mock_test_7, mock_test_8, mock_test_9, mock_test_10, prediction # type: ignore

st.set_page_config(
    page_title="NEET Qualifying Portal",
)

class MultiApp:

    def __init__(self):
        self.apps = []

    def add_app(self, title, func):
        self.apps.append({
            "title": title,
            "function": func
        })

    def run(self):  # Add self parameter here
        with st.sidebar:        
            app = option_menu( # type: ignore
                menu_title='NEET Qualifying Portal',
                options=['Home', 'Account', 'Mock', 'Mock_Test_1', 'Mock_Test_2', 'Mock_Test_3', 'Mock_Test_4', 'Mock_Test_5', 'Mock_Test_6', 'Mock_Test_7', 'Mock_Test_8', 'Mock_Test_9', 'Mock_Test_10', 'Prediction'],
                icons=['house-fill', 'person-circle','star-fill', 'star', 'star', 'star', 'star', 'star', 'star', 'star', 'star', 'star','star', 'info-circle'],  # Adjusted the icons list
                menu_icon='chat-text-fill',
                default_index=1,
                styles={
                    "container": {"padding": "5!important", "background-color": 'black'},
                    "icon": {"color": "white", "font-size": "23px"}, 
                    "nav-link": {"color": "white", "font-size": "20px", "text-align": "left", "margin": "0px", "--hover-color": "blue"},
                    "nav-link-selected": {"background-color": "#02ab21"},
                }
            )

        if app == "Home":
            home.app()
        if app == "Account":
            account.app()
        if app == "Mock":
            mock.app()
        if app == "Mock_Test_1":
            mock_test_1.app()
        if app == "Mock_Test_2":
            mock_test_2.app()
        if app == "Mock_Test_3":
            mock_test_3.app()
        if app == "Mock_Test_4":
            mock_test_4.app()
        if app == "Mock_Test_5":
            mock_test_5.app()
        if app == "Mock_Test_6":
            mock_test_6.app()
        if app == "Mock_Test_7":
            mock_test_7.app()
        if app == "Mock_Test_8":
            mock_test_8.app()
        if app == "Mock_Test_9":
            mock_test_9.app()
        if app == "Mock_Test_10":
            mock_test_10.app()    
        if app == "Prediction":
            prediction.app()        

multi_app = MultiApp()  # Create an instance of MultiApp
multi_app.run()  # Call the run method of MultiApp instance