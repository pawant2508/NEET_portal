import streamlit as st
from streamlit_option_menu import option_menu
import home, account, mock, mock_test_1, mock_test_2, mock_test_3, mock_test_4, mock_test_5, mock_test_6, mock_test_7, mock_test_8, mock_test_9, mock_test_10, prediction

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

    def option_menu(self):  # Corrected the method signature
        menu_title = 'NEET Qualifying Portal'
        options = ['Home', 'Account', 'Mock', 'Mock_Test_1', 'Mock_Test_2', 'Mock_Test_3', 'Mock_Test_4', 'Mock_Test_5', 'Mock_Test_6', 'Mock_Test_7', 'Mock_Test_8', 'Mock_Test_9', 'Mock_Test_10', 'Prediction']
        selected_option = st.sidebar.selectbox(menu_title, options)

        # Call the corresponding app function based on the selected option
        if selected_option == 'Home':
            home.app()
        elif selected_option == 'Account':
            account.app()
        elif selected_option == 'Mock':
            mock.app()
        elif selected_option == 'Mock_Test_1':
            mock_test_1.app()
        elif selected_option == 'Mock_Test_2':
            mock_test_2.app()
        elif selected_option == 'Mock_Test_3':
            mock_test_3.app()
        elif selected_option == 'Mock_Test_4':
            mock_test_4.app()
        elif selected_option == 'Mock_Test_5':
            mock_test_5.app()
        elif selected_option == 'Mock_Test_6':
            mock_test_6.app()
        elif selected_option == 'Mock_Test_7':
            mock_test_7.app()
        elif selected_option == 'Mock_Test_8':
            mock_test_8.app()
        elif selected_option == 'Mock_Test_9':
            mock_test_9.app()
        elif selected_option == 'Mock_Test_10':
            mock_test_10.app()
        elif selected_option == 'Prediction':
            prediction.app()

multi_app = MultiApp()
multi_app.option_menu()
