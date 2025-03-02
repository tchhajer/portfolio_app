import os
import streamlit as st
import base64

# Page configuration
st.set_page_config(
    page_title='Vijayram Patel - Portfolio',
    layout="wide",
    page_icon='👨‍💻'
)

# Initialize session state to track the current section
if 'section' not in st.session_state:
    st.session_state.section = 'About Me'  # Default section is 'About Me'

# Function to render the "About Me" section
def render_about_me():
    st.title('Hi, I am Vijayram Patel! 👋')
    st.write("Master's in Information student at the University of Wisconsin-Madison with a passion for Data Engineering, Machine Learning, and Analytics.")
    st.write("With over a year of professional experience, I specialize in Python, SQL, Spark, AWS, and Data Visualization.")
    st.markdown("**Email:** [vpatel57@wisc.edu](mailto:vpatel57@wisc.edu)")
    st.markdown("**LinkedIn:** [linkedin.com/in/vijayram-patel](https://www.linkedin.com/in/vijayram-patel/)")
    st.markdown("**GitHub:** [github.com/vijayrampatel](https://github.com/vijayrampatel)")

# Function to render projects
def render_projects():
    st.title("Projects")
    st.subheader("Redfin Housing Data Pipeline and Visualization")
    st.write("Built an end-to-end data pipeline using Python, AWS, Snowflake, and Apache Airflow, providing an interactive dashboard.")
    st.subheader("Kafka Data Pipeline")
    st.write("Developed a real-time data pipeline for event processing and analytics.")
    st.subheader("Fraud Transaction Detection")
    st.write("Applied Machine Learning models to detect fraudulent transactions.")

# Function to render skills
def render_skills():
    st.title("Skills")
    st.write("**Programming:** Python, SQL, Spark, JavaScript, C")
    st.write("**Cloud & Databases:** AWS (S3, RDS, DynamoDB), GCP, Snowflake, Databricks")
    st.write("**Tools & Frameworks:** Tableau, Airflow, TensorFlow, PyTorch, Docker")

# Create navigation buttons
col1, col2, col3 = st.columns(3)

with col1:
    if st.button('About Me'):
        st.session_state.section = 'About Me'

with col2:
    if st.button('Projects'):
        st.session_state.section = 'Projects'

with col3:
    if st.button('Skills'):
        st.session_state.section = 'Skills'


# Render the selected section
if st.session_state.section == 'About Me':
    render_about_me()
elif st.session_state.section == 'Projects':
    render_projects()
elif st.session_state.section == 'Skills':
    render_skills()

