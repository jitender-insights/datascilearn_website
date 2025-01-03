
import streamlit as st
from PIL import Image

def show_home():
    # Banner GIF
    st.image("assets/banner.gif", use_container_width=True)

    # Welcome Section
    st.title("🎉 Welcome to DataSciLearn")
    st.markdown("""
        **Let's Learn Data Science!**  
        DataSciLearn is your go-to platform for:
        - 🌟 Generative AI Tutorials
        - 📈 Data Science Projects
        - 🧠 Machine Learning Insights
    """)

    # Call-to-action buttons with logos
    st.markdown(
        """
        <style>
        .platform-buttons {
            display: flex;
            justify-content: center;
            gap: 20px;
            margin-top: 20px;
        }
        .platform-buttons a {
            text-decoration: none;
        }
        .platform-buttons img {
            width: 50px;
            height: 50px;
            transition: transform 0.2s;
        }
        .platform-buttons img:hover {
            transform: scale(1.2); /* Enlarge icon on hover */
        }
        </style>
        <div class="platform-buttons">
            <a href="https://www.youtube.com/@datascilearn" target="_blank">
                <img src="https://upload.wikimedia.org/wikipedia/commons/4/42/YouTube_icon_%282013-2017%29.png" alt="YouTube">
            </a>
            <a href="https://t.me/datascilearn" target="_blank">
                <img src="https://upload.wikimedia.org/wikipedia/commons/8/83/Telegram_2019_Logo.svg" alt="Telegram">
            </a>
            <a href="https://www.instagram.com/datascilearn/" target="_blank">
                <img src="https://upload.wikimedia.org/wikipedia/commons/a/a5/Instagram_icon.png" alt="Instagram">
            </a>
            <a href="https://www.linkedin.com/company/datascilearn" target="_blank">
                <img src="https://upload.wikimedia.org/wikipedia/commons/c/ca/LinkedIn_logo_initials.png" alt="LinkedIn">
            </a>
        </div>
        """,
        unsafe_allow_html=True
    )


