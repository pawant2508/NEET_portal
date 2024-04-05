import streamlit as st  # type: ignore

def app():
    st.title("NEET Exam Mock Test Site")

    st.write(
        """
        Welcome to the NEET Exam Mock Test Site! This platform allows you to practice for the NEET exam
        by taking mock tests and assessing your performance. You can also access various resources and tools
        to help you prepare effectively.
        """
    )

    st.write("### Get Started")
    st.write(
        """
        To begin, select one of the following options:
        - **Take a Mock Test:** Start practicing by taking a mock test.
        - **View Study Materials:** Access study materials and resources for NEET preparation.
        - **Track Progress:** Monitor your performance and track your progress over time.
        - **Explore More:** Discover additional features and functionalities of the platform.
        """
    )

    st.write("### Mock Test Guidelines")
    st.write(
        """
        For conducting a mock test for your final year project, considering the parameters you've mentioned, here are the guidelines you can follow:
        1. Duration: Allocate 3 hours of time for the mock test, mirroring the actual NEET exam duration.

        2. Total Marks: Set the total marks for the mock test to 720, aligning with the NEET exam's total marks.

        3. Question Format: Design the mock test with a variety of question formats, including multiple-choice questions, match the following, assertion-reasoning, etc., similar to the NEET exam pattern.

        4. Negative Marking: Implement negative marking of 1/4 for incorrect answers to simulate the NEET exam's marking scheme accurately.

        5. Question Distribution: Distribute the questions across the relevant subjects, such as Physics, Chemistry, and Biology, according to the NEET syllabus.

        6. Difficulty Level: Ensure that the difficulty level of the questions reflects that of the actual NEET exam, with some easy, moderate, and challenging questions.

        7. Instructions: Provide clear instructions to the participants regarding the rules of the mock test, including the marking scheme, time allocation, and any specific guidelines.

        8. Mock Test Platform: Choose a suitable platform or method for administering the mock test, whether it's through an online portal, paper-based format, or any other means feasible for your project.

        9. Analysis and Evaluation: Analyze the results of the mock test to assess the effectiveness of your project in simulating the NEET exam experience and identify any areas for refinement or enhancement.

        By following these guidelines, you can effectively conduct a mock test for your final year project, providing valuable insights into the participants' preparedness for the actual NEET exam.
        """
    )

    st.write("### About NEET")
    st.write(
        """
        The National Eligibility cum Entrance Test (NEET) is an entrance examination in India
        for students who wish to study undergraduate medical courses (MBBS) and dental courses (BDS)
        in government or private medical colleges in India. NEET is conducted by the National Testing Agency (NTA).

        The National Testing Agency (NTA) is responsible for conducting the NEET exam on behalf of the Ministry of Health and Family Welfare, Government of India.

        NEET is a highly competitive exam, and aspirants are advised to start their preparation early and remain focused and dedicated throughout the process. It is essential to stay updated with exam-related information, follow a disciplined study routine, and seek guidance from experienced mentors or coaching institutes for effective preparation.
        
        NEET is a pen-and-paper-based exam (offline mode) consisting of a single question paper with multiple-choice questions (MCQs).
        The exam duration is 3 hours.
        The question paper comprises 180 questions, with 45 questions each from Physics, Chemistry, and Biology (Botany & Zoology).
        Each correct answer carries 4 marks, while an incorrect answer results in a deduction of 1 mark (negative marking).

        To appear for the NEET exam, candidates must fulfill the following eligibility criteria:
        Age: Candidates must be at least 17 years old at the time of admission or will be 17 years old on or before December 31 of the year of admission.
        Qualification: Candidates must have completed or are in the process of completing their 10+2 or equivalent examination with Physics, Chemistry, Biology/Biotechnology, and English as core subjects.
        Minimum Marks: Candidates must secure minimum qualifying marks in their qualifying examination (usually 50% for general category and 40% for reserved categories).

        """
    )

    st.write("### Contact Us")
    st.write(
        """
        If you have any questions or feedback, please feel free to reach out to us:
        - **Email:** contact@neetmocktestsite.com
        - **Phone:** +91-XXXXXXXXXX
        """
    )

if __name__ == "__main__":
    app()
