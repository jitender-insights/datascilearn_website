import streamlit as st

def show_contact():
    # Contact Section
    st.markdown(
        """
        ## 🌐 Connect with Us

        Follow us on our social media channels to stay updated and be part of the community!

        <style>
        .contact-links {
            display: flex;
            flex-direction: column;
            align-items: flex-start;
            gap: 10px;
            margin-top: 20px;
        }
        .contact-links a {
            font-size: 16px;
            color: #4CAF50;
            text-decoration: none;
            font-weight: bold;
        }
        .contact-links a:hover {
            text-decoration: underline;
        }
        </style>
        <div class="contact-links">
            <a href="https://www.instagram.com/datascilearn/" target="_blank">📷 Instagram</a>
            <a href="https://www.youtube.com/@datascilearn" target="_blank">📣 YouTube</a>
            <a href="https://t.me/datascilearn" target="_blank">📺 Telegram</a>
            <a href="https://www.linkedin.com/company/datascilearn" target="_blank">🔗 LinkedIn</a>
        </div>
        """,
        unsafe_allow_html=True
    )
