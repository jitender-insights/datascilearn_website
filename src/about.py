import streamlit as st
def show_about():
    st.title("📖 About Us")
    col1, col2 = st.columns([1, 2])

    # Add a personal photo or logo
    with col1:
        st.image("assets/logo.png", width=200)

    # About text
    with col2:
        st.markdown("""
        **DataSciLearn** is a free platform for data science enthusiasts to:
        - Learn about AI/ML, Generative AI, and Data Science.
        - Build real-world projects.
        - Connect with a growing community of learners.
        ---
        """)

