import streamlit as st

def show_courses():
    st.title("Available Courses")
    
    # Display a list of available courses with buttons or links
    st.subheader("Course 1: Data Science Master")
    st.write("Data Science Bootcamp.")
    if st.button("View Playlist for Course 1"):
        show_course_1()
    
    st.subheader("Course 2: Generative AI Master")
    st.write("Genertaive AI Bootcamp.")
    if st.button("View Playlist for Course 2"):
        show_course_2()

    st.subheader("Course 3: MLOps Basic to Advanced ")
    st.write("MLOps Bootcamp.")
    if st.button("View Playlist for Course 3"):
        show_course_3()

def show_course_1():
    st.title("Course 1: Data Science Master")
    
    # Embed YouTube Playlist 1
    st.markdown("""
        <div style="text-align: center;">
            <iframe width="100%" height="315" src="https://www.youtube.com/embed/videoseries?list=PLCr2JQj_VZZpGaw6SL-9_dmrhIRbAm5qv"  
            frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" 
            allowfullscreen></iframe>
        </div>
    """, unsafe_allow_html=True)

def show_course_2():
    st.title("Course 2: Generative AI Master")
    
    # Embed YouTube Playlist 2
    st.markdown("""
        <div style="text-align: center;">
            <iframe width="100%" height="315" src="https://www.youtube.com/embed/videoseries?list=PLCr2JQj_VZZpipJWtSqRt9T9l4Guh--MN" 
            frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" 
            allowfullscreen></iframe>
        </div>
    """, unsafe_allow_html=True)

def show_course_3():
    st.title("Course 3: MLOps Basic to Advanced")
    
    # Embed YouTube Playlist 3
    st.markdown("""
        <div style="text-align: center;">
            <iframe width="100%" height="315" src="https://www.youtube.com/embed/videoseries?list=PLCr2JQj_VZZqvB2eyd4NvsDTsfMjVqaDi" 
            frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" 
            allowfullscreen></iframe>
        </div>
    """, unsafe_allow_html=True)
