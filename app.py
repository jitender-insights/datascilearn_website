
import streamlit as st
from src.home import show_home
from src.about import show_about
from src.projects import show_projects
from src.contact import show_contact
from src.courses import show_courses

# Apply custom CSS
with open("assets/styles.css") as f:
    st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

# Sidebar Navigation
st.sidebar.image("assets/logo.png", width=150)
st.sidebar.title("DataSciLearn")
page = st.sidebar.radio("Navigate", ["Home", "About", "Projects", "Contact","Courses"])

# Routing
if page == "Home":
    show_home()
elif page == "About":
    show_about()
elif page == "Projects":
    show_projects()
elif page == "Contact":
    show_contact()
elif page == "Courses":
    show_courses()
    


# Footer
st.markdown(
    """
    <style>
    .footer {
        position: fixed;
        left: 0;
        bottom: 0;
        width: 100%;
        background-color: #0E1117;
        color: #FAFAFA;
        text-align: center;
        padding: 10px;
        font-size: 14px;
        box-shadow: 0px -1px 5px rgba(0, 0, 0, 0.2);
        z-index: 1000;
    }
    .footer a {
        color: #4CAF50;
        text-decoration: none;
    }
    .footer a:hover {
        text-decoration: underline;
    }
    </style>
    <div class="footer">
        Created with ❤️ by <b>DataSciLearn</b> | 
        <a href="https://github.com/jitender-insights" target="_blank">GitHub</a>
    </div>
    """,
    unsafe_allow_html=True
)


