import os
import streamlit as st
import base64
import requests
from streamlit_option_menu import option_menu
from pathlib import Path
 
# Set page config
st.set_page_config(
    page_title='Portfolio',
    layout="wide",
    page_icon='👧🏻'
)
 
# Set default section
if 'section' not in st.session_state:
    st.session_state.section = 'About Me'
 
def side_page():
    def get_image_base64(image_path):
        with open(image_path, "rb") as image_file:
            return base64.b64encode(image_file.read()).decode('utf-8')
 
    img_base64 = get_image_base64("assets/images/photo.png")
 
    st.markdown("""
    <style>
        .main {{
            text-align: center;
        }}
        .profile-img {{
            width: 200px;
            height: 200px;
            border-radius: 50%;
            object-fit: cover;
            border: 3px solid #333;
        }}
        .name {{
            font-size: 2rem;
            font-weight: bold;
        }}
        .title {{
            color: #aaa;
        }}
        .contact-item {{
            margin-top: 1rem;
        }}
    </style>
    <div class="main">
        <div><img src="data:image/png;base64,{0}" class="profile-img"></div>
        <div class="name">Vijayram Patel</div>
        <div class="title">Machine Learning & Analytics</div>
        <div class="contact-item">📧 vpatel57@wisc.edu</div>
        <div class="contact-item">📞 +1 (608) 239-0675</div>
        <div class="contact-item">📍 Madison, Wisconsin</div>
        <div class="contact-item">
            <a href="https://www.linkedin.com/in/vijayram-patel/" target="_blank">LinkedIn</a> |
            <a href="https://github.com/vijayrampatel" target="_blank">GitHub</a>
        </div>
    </div>
               
    """.format(img_base64), unsafe_allow_html=True)
 
def render_about_me():
    col1, col2, col3 = st.columns([7,1,20])
    with col1:
        side_page()
    with col2:
        pass
    with col3:
        st.title('Hi, I am Arya! 👋')
        st.write('''
I'm Vijayram Patel, a Master's in Information student at UW-Madison specializing in data engineering and analytics.
I am an AWS certified Data Engineer with professional experience in both research and industry settings.
I transform complex data into actionable insights using Python, SQL, AWS, and various data visualization tools.
My expertise spans machine learning, data pipeline development, and business intelligence.
        ''')
 
def render_research_experience():
    col1, col2, col3 = st.columns([7,1,20])
    with col1:
        side_page()
    with col2:
        pass
    with col3:
        st.header("Work Experience")
 
        experiences = [
            {
                "title": "Data Analyst",
                "subtitle": "Universities of Wisconsin System",
                "date": "Jun 2024 - Aug 2024",
                "details": [
                    "Delivered insights and improved data processes.",
                    "Engineered pipelines using Airbyte, Snowflake, dbt.",
                    "Built Tableau dashboards to guide $100M+ in grants."
                ],
            },
            {
                "title": "Research Assistant",
                "subtitle": "UW-Madison SMPH",
                "date": "Sep 2021 - Sep 2022",
                "details": [
                    "Analyzed 27 years of dermatology data.",
                    "Improved care efficiency by 25% via KPIs.",
                    "Performed p-values, hypothesis testing."
                ],
            },
        ]
 
        for exp in experiences:
            st.markdown(f"""
            **{exp['title']}**  
            *{exp['subtitle']}* ({exp['date']})
           
            - {exp['details'][0]}
            - {exp['details'][1]}
            - {exp['details'][2]}
            """)
 
def projects():
    col1, col2, col3 = st.columns([7,1,20])
    with col1:
        side_page()
    with col2:
        pass
    with col3:
        st.header("Projects")
 
        projects = [
            {"title": "Kafka Data Pipeline", "description": "Real Time Analytics"},
            {"title": "Movie Recommendation System", "description": "NLP and Deep Learning"}
        ]
 
        for project in projects:
            st.subheader(project["title"])
            st.write(project["description"])
 
def resume():
    resume_path = "https://drive.google.com/file/d/1o8ir0stxEk26neHUrV-jXNC6zee3aIOW/view?usp=drive_link"
    import webbrowser
    webbrowser.open_new_tab(resume_path)
    st.info("Opening resume in a new tab. If it doesn't open automatically, [click here](%s)" % resume_path)
    st.write("My resume provides details about my education, skills, and work experience.")
 
def contact():
    col1, col2, col3 = st.columns([7,1,20])
    with col1:
        side_page()
    with col2:
        pass
    with col3:
        st.header("Contact")
 
        full_name = st.text_input("Full Name")
        email = st.text_input("Email")
        message = st.text_area("Message")
 
        if st.button("Send"):
            if full_name and email and message:
                st.success("Message sent successfully!")
            else:
                st.error("Please fill all fields.")
 
selected_tab = option_menu(
    menu_title=None,
    options=["About Me", "Technical Experience", "Projects", "Resume", "Contact"],
    icons=["person", "briefcase", "folder", "info", "envelope"],
    menu_icon="cast",
    default_index=0,
    orientation="horizontal",
)
 
if selected_tab == 'About Me':
    render_about_me()
elif selected_tab == 'Technical Experience':
    render_research_experience()
elif selected_tab == 'Projects':
    projects()
elif selected_tab == 'Resume':
    resume()
elif selected_tab == 'Contact':
    contact()
 