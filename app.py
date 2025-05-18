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
        .main {
            text-align: center;
        }
        .profile-img {
            width: 200px;
            height: 200px;
            border-radius: 50%;
            object-fit: cover;
            border: 3px solid #333;
        }
        .name {
            font-size: 2rem;
            font-weight: bold;
        }
        .title {
            color: #aaa;
        }
        .contact-item {
            margin-top: 1rem;
        }
    </style>
    """, unsafe_allow_html=True)

    st.markdown(f'''
        <div class="main">
            <img src="data:image/png;base64,{img_base64}" class="profile-img">
            <div class="name">Tejas Chhajer</div>
            <div class="title">Mechanical Engineer</div>
            <div class="contact-item"><strong>Email:</strong><br>chhajertejas@gmail.com</div>
            <div class="contact-item"><strong>Phone:</strong><br>+1 (917) 519-2300</div>
            <div class="contact-item"><strong>Location:</strong><br>Chicago, Illinois</div>
            <div class="contact-item">
                <a href="https://www.linkedin.com/in/tejaschhajer/" target="_blank">LinkedIn</a> |
                <a href="https://github.com/tchhajer" target="_blank">GitHub</a>
            </div>
        </div>
    ''', unsafe_allow_html=True)

def render_about_me():
    col1, col2, col3 = st.columns([7,1,20])
    with col1:
        side_page()
    with col3:
        st.title('Hi, I am Tejas! 👋')
        st.markdown('''
<div style="text-align: left; font-size: 16px;">
    <p>I’m a Mechanical Engineer with a strong passion for innovation, efficiency, and strategy. I recently graduated from UW–Madison, where I specialized in manufacturing and operations. Throughout my internships at Doosan Bobcat and Vertiv, I worked on high-impact projects — from streamlining production processes to contributing to executive-level strategy presentations.</p>
    <p>I enjoy bridging the gap between technical engineering and business strategy. Whether I’m optimizing a paint line workflow, presenting to senior leadership, or mentoring new interns, I bring a can-do spirit and a focus on results.</p>
    <p>I’m actively seeking full-time roles in manufacturing engineering, operations, or strategy, where I can continue solving real-world problems with creativity and precision.</p>
</div>
''', unsafe_allow_html=True)
def render_research_experience():
    col1, col2, col3 = st.columns([7, 1, 20])
    with col1:
        side_page()
    with col3:
        st.markdown("<h1 style='margin-bottom: 20px; text-align: center;'>Work Experience</h1>", unsafe_allow_html=True)

        st.markdown("""
            <style>
                .exp-entry {
                    margin-bottom: 2rem;
                    text-align: left;
                }
                .exp-title {
                    font-size: 1.2rem;
                    font-weight: bold;
                    margin-bottom: 0.2rem;
                }
                .exp-subtitle {
                    font-style: italic;
                    margin-bottom: 0.2rem;
                }
                .exp-date {
                    color: gray;
                    font-size: 0.9rem;
                    margin-bottom: 0.5rem;
                }
                .exp-details {
                    padding-left: 1.2rem;
                }
                .exp-details li {
                    margin-bottom: 0.4rem;
                }
            </style>
        """, unsafe_allow_html=True)

        experiences = [
            {
                "title": "Advanced Manufacturing Engineering Intern, AC Power",
                "subtitle": "Vertiv - Delaware, OH",
                "date": "May 2024 - Aug 2024",
                "details": [
                    "Created AutoCAD layouts for system level integration in NPI, optimizing product lifecycle & serviceability",
                    "Developed factory readiness planning tool on Excel for inventory, layout, and ramp-up KPIs using SIOP, VSM & time studies",
                    "Developed new Lean-based processes for integrating wall panels, air conditioning units & overhead bus-way channels",
                    "Reduced alignment quality defects by 70% by designing a bus bar guiding tool on CREO using GD&T & DFM principles",
                    "Prevented a 3-month shipping delay by applying RCA & rapid prototyping a 3D printed part, approved for production",
                    "Designed & integrated wire harnesses & connectors for mobile electric test carts to test the DC battery cabinets"
                ],
            },
            {
                "title": "Manufacturing Co-op, Ops. Strategy & Advanced Manufacturing",
                "subtitle": "Doosan Bobcat - Bismarck, ND",
                "date": "May 2023 - May 2024",
                "details": [
                    "Trained a new hire on Ansys & FEA-based weld deformation simulation & documented best practices",
                    "Developed, tested & validated welding deformation simulation using Ansys & ESI SysWeld",
                    "Reduced deformation of weldments by 20% by conducting FEA-based structural & thermal analysis on Ansys & ESI SysWeld",
                    "Introduced welding simulation capability in a company-wide knowledge-sharing event",
                    "Pitched a new suspension platform on Mini-Track Loader (MTL) prototype to CEO, company executives & customers",
                    "Created MBOM structure & SOP and used MES for system level integration of new mower line",
                    "Implemented 5S & lean practices by designing & fabricating workshop equipment: saw table, tube rack, workbench & storage"
                ],
            },
            {
                "title": "Research Assistant",
                "subtitle": "UW Madison: Nellis Cryogenic Lab",
                "date": "Jan, 2022 - May, 2022",
                "details": [
                    "Conducted experiments to measure the heat transfer rate through copper at cryogenic temperatures as low as 4 K",
                    "Setup the test rig by wiring thermocouple sensors & utilized EES to collect & process raw data"                    
                ],
            },
            {
                "title": "Student Supervisor",
                "subtitle": "Gordon Dining and Event Center - Madison, WI",
                "date": "Aug, 2021 - May, 2023",
                "details": [
                    "Oversaw employee training, performance management & process improvement while serving 2000+ customers"
                ],
            }
        ]

        for exp in experiences:
            bullet_points = "".join(f"<li>{item}</li>" for item in exp['details'])

            st.markdown(f"""
                <div class="exp-entry">
                    <div class="exp-title">{exp['title']} - <span class="exp-subtitle">{exp['subtitle']}</span></div>
                    <div class="exp-date">{exp['date']}</div>
                    <ul class="exp-details">
                        {bullet_points}
                    </ul>
                </div>
            """, unsafe_allow_html=True)

def projects():
    col1, col2, col3 = st.columns([7,1,20])
    with col1:
        side_page()
    with col3:
        st.markdown("<h1 style='margin-bottom: 20px;'>Projects</h1>", unsafe_allow_html=True)

        project_data = [
            {"title": "Kafka Data Pipeline", "description": "Real Time Analytics"},
            {"title": "Movie Recommendation System", "description": "NLP and Deep Learning"}
        ]

        for project in project_data:
            st.subheader(project["title"])
            st.write(project["description"])

def resume():
    resume_path = "https://drive.google.com/file/d/1o8ir0stxEk26neHUrV-jXNC6zee3aIOW/view?usp=drive_link"
    st.markdown(f"""
        <script>
            window.open("{resume_path}", "_blank");
        </script>
    """, unsafe_allow_html=True)
    st.info("Opening resume in a new tab. If it doesn't open automatically, [click here](%s)" % resume_path)

def contact():
    col1, col2, col3 = st.columns([7,1,20])
    with col1:
        side_page()
    with col3:
        st.markdown("<h1 style='margin-bottom: 20px;'>Contact</h1>", unsafe_allow_html=True)

        full_name = st.text_input("Full Name", placeholder="Enter your full name")
        email = st.text_input("Email", placeholder="Enter your email address")
        message = st.text_area("Message", placeholder="Type your message here...")

        if st.button("Send"):
            if full_name and email and message:
                st.success("Message sent successfully!")
            else:
                st.error("Please fill all fields.")

selected_tab = option_menu(
    menu_title=None,
    options=["About Me", "Work Experience", "Projects", "Resume", "Contact"],
    icons=["person", "briefcase", "folder", "info", "envelope"],
    menu_icon="cast",
    default_index=0,
    orientation="horizontal",
)

if selected_tab == 'About Me':
    render_about_me()
elif selected_tab == 'Work Experience':
    render_research_experience()
elif selected_tab == 'Projects':
    projects()
elif selected_tab == 'Resume':
    resume()
elif selected_tab == 'Contact':
    contact()