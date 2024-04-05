import streamlit as st # type: ignore
from firebase_admin import firestore # type: ignore
import firebase_admin # type: ignore
import random

# Check if Firebase app is already initialized
if not firebase_admin._apps:
    # Initialize Firebase app
    firebase_admin.initialize_app()

def generate_possible_score(score_range):
    return random.randint(score_range[0], score_range[1])

def determine_qualification(possible_score, category):
    if category in ["UR", "OBC"]:
        if 600 <= possible_score <= 720:
            return "High Chance of Qualification", possible_score
        elif 400 <= possible_score < 600:
            return "Moderate Chance of Qualification", possible_score
        else:
            return "Unlikely to Qualify", possible_score
    elif category == "SC":
        if possible_score >= 250:
            return "Moderate Chance of Qualification", possible_score
        else:
            return "Unlikely to Qualify", possible_score
    elif category == "ST":
        if possible_score >= 300:
            return "Moderate Chance of Qualification", possible_score
        else:
            return "Unlikely to Qualify", possible_score
    elif category == "EWS":
        if 550 <= possible_score <= 720:
            return "High Chance of Qualification", possible_score
        elif 350 <= possible_score < 550:
            return "Moderate Chance of Qualification", possible_score
        else:
            return "Unlikely to Qualify", possible_score
    else:
        return "Invalid Category", possible_score

def app():
    # Initialize Firestore client
    db = firestore.client()

    # Check if user is logged in
    if 'username' not in st.session_state or not st.session_state['username']:
        st.error('Please login first.')
        return

    try:
        st.title("NEET Qualification Predictor")

        # Select category
        category = st.selectbox("Select Category", ["UR", "OBC", "SC", "ST", "EWS"])

        if 'mock_test_scores' not in st.session_state:
            st.session_state.mock_test_scores = []

        for i in range(10):
            possible_score = st.number_input(f"Enter Mock Test {i+1} score", min_value=0, max_value=720, step=1, value=None,
                                             key=f"mock_test_score_{i}")
            if possible_score is not None:
                st.session_state.mock_test_scores.append(possible_score)

        if st.button("Generate Possible Score"):
            score_range = (300, 720)  # Define the range of possible scores
            possible_score = generate_possible_score(score_range)
            st.write("Possible Score:", possible_score)

            # Randomly select a category
            categories = ["UR", "OBC", "SC", "ST", "EWS"]
            category = random.choice(categories)

            # Determine qualification based on the generated possible score and selected category
            qualification = determine_qualification(possible_score, category)
            st.write("NEET Qualification:", qualification)

    except Exception as e:
        st.error(f"An error occurred: {e}")

if __name__ == "__main__":
    app()