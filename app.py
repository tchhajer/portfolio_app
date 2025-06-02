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

    img_base64 = get_image_base64("assets/images/project1.jpg")

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
    <p>I’m a Mechanical Engineer with a strong passion for innovation, efficiency, and strategy. I recently graduated from UW–Madison, where I specialized in manufacturing and operations. Throughout my internships at Doosan Bobcat and Vertiv, I led high-impact projects, from streamlining production processes using Lean manufacturing and Six Sigma principles to contributing to executive-level strategy presentations through data-driven analysis.</p>
    <p>I enjoy bridging the gap between technical engineering and business strategy. Whether I’m optimizing a paint line workflow using value stream mapping and time studies, presenting to senior leadership with actionable KPIs, or mentoring new interns on CAD modeling and process documentation, I bring a can-do spirit and a focus on results.</p>
    <p>I’m actively seeking full-time roles in manufacturing engineering, operations, or strategy, where I can continue solving real world problems with creativity and precision. My technical toolkit includes proficiency in SolidWorks, AutoCAD, FEA, GD&T, ERP systems (like SAP), and continuous improvement methodologies.</p>
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
    st.markdown("<h1 style='margin-bottom: 20px;'>Projects</h1>", unsafe_allow_html=True)

    categories = ["All", "Design & Fabrication", "FEA & Simulation", "Manufacturing Planning & Optimization"]
    selected_category = st.radio("Filter by category:", categories, horizontal=True)

    project_data = [
        {
            "title": "Weld Deformation Simulation",
            "description": "Developed and validated a comprehensive welding deformation simulation using Ansys and ESI SysWeld. The project aimed to predict thermal distortion in welded structures and implement mitigation strategies, ultimately reducing post-weld defects and improving part accuracy. Results from simulation were benchmarked against physical measurements to ensure model reliability.",
            "category": "FEA & Simulation",
            "image": "assets/images/weld_deformation1.png",
            "github_link": "https://github.com/tchhajer/Weld-Deformation-software-development-and-validation"
        },
        {
            "title": "Mini-Track Loader Platform",
            "description": "Designed and developed a height-adjustable platform for a Mini-Track Loader using a 4-bar linkage suspension system to improve ride comfort and operator ergonomics. The concept, now patent pending, enables smoother operation and greater versatility on job sites.",
            "category": "Design & Fabrication",
            "image": "assets/images/mtl_platform1.png",
            "github_link": "https://github.com/tchhajer/Platform-for-Mini-Track-Loader"
        },
        {
            "title": "Guide Tool",
            "description": "Developed a precision alignment tool to assist in the assembly of busbars within lithium-ion battery cabinets at Vertiv. Through rapid prototyping and user-driven ergonomic improvements, the 3D-printed tool reduced alignment-related quality defects from 10% to 0%, eliminated rework, and significantly improved workflow efficiency. The tool helped save substantial costs associated with scrap, rework, and production delays.",
            "category": "Design & Fabrication",
            "image": "assets/images/guide_tool.png",
            "github_link": "https://github.com/tchhajer/Guide-tool"
        },
        {
            "title": "Modular Data Center Integration Plan",
            "description": "Developed a comprehensive AutoCAD-based layout and integration strategy for the production of a large-scale modular data center for a high-profile client. The plan included a detailed work schedule timeline, precise staging area positioning, and a visual installation sequence tailored to a space-constrained environment. The result was an easy-to-follow guide that enabled efficient production execution and seamless coordination across teams.",
            "category": "Manufacturing Planning & Optimization",
            "image": "assets/images/integration.jpg",
            "github_link": "https://github.com/tchhajer/Integration-plan-for-Modular-data-center"
        },
        {
            "title": "Trinergy Production Line Setup",
            "description": "Created a detailed production line layout for Trinergy UPS systems, focusing on optimizing material flow and space utilization. Conducted in-depth evaluations of module movement paths to minimize handling time and bottlenecks. Proposed and integrated a vertical storage unit into the layout to maximize floor space and support just-in-time accessibility. The finalized plan supported streamlined assembly operations and improved overall shop floor organization.",
            "category": "Manufacturing Planning & Optimization",
            "image": "assets/images/trinergy.png",
            "github_link": "https://github.com/tchhajer/trinergy-Production-line-setup"
        },
        {
            "title": "Plug Plates",
            "description": "Designed and rapidly prototyped custom plug plates using 3D printing to resolve a critical supply chain issue for a high-profile UPS order. The original component was delayed due to procurement bottlenecks, and the engineered replacement matched the original specifications closely enough to be used in production. This solution helped avoid shipping delays and ensured timely delivery to the customer.",
            "category": "Design & Fabrication",
            "image": "assets/images/plugplate.png",
            "github_link": "https://github.com/tchhajer/Plug-Plates"
        },
        {
            "title": "Welding Storage Rack",
            "description": "Redesigned an improved version of the standard Bluco welding storage rack by incorporating operator feedback. The solution increased available storage space, improved accessibility, and included mobility features for flexible use on the shop floor. The final design was also optimized for ease of fabrication and cost efficiency.",
            "category": "Design & Fabrication",
            "image": "assets/images/bluco_rack.png",
            "github_link": "https://github.com/tchhajer/Welding-Storage-Rack"
        },
        {
            "title": "Tube Storage Rack",
            "description": "Designed and fabricated a vertical storage rack to organize long metal tubes efficiently while improving shop floor ergonomics. By utilizing unused vertical space, the solution reclaimed valuable floor area, reduced clutter, and enhanced accessibility for operators. The rack was integrated as part of a broader Lean 5S initiative to improve workspace layout and efficiency.",
            "category": "Design & Fabrication",
            "image": "assets/images/tube_rack.png",
            "github_link": "https://github.com/tchhajer/Tube-Storage-Rack"
        },
        {
            "title": "Table with Saw Cutter Attachment",
            "description": "Designed and fabricated a heavy-duty worktable with an integrated saw cutter to streamline fabrication tasks. The setup reduced operator walking time, improved safety, and supported 5S implementation by consolidating cutting operations into a dedicated ergonomic station.",
            "category": "Design & Fabrication",
            "image": "assets/images/newtable.png",
            "github_link": "https://github.com/tchhajer/Table-with-saw-cutter-attachment"
        },
        {
            "title": "Scrap Tube Storage Cart",
            "description": "Fabricated a mobile scrap tube cart to streamline material handling and waste management on the shop floor. Designed with Lean principles in mind, it reduced clutter, enabled point-of-use collection, and contributed to floor space optimization under 5S guidelines.",
            "category": "Design & Fabrication",
            "image": "assets/images/tube_cart.png",
            "github_link": "https://github.com/tchhajer/Scrap-Tube-storge-cart"
        },
        {
            "title": "Engine Cherry Picker",
            "description": "Engineered and built a hydraulic cherry picker for safely lifting and maneuvering heavy engine components. This shop-built tool improved assembly ergonomics, minimized manual handling risks, and supported Lean workflow by enabling mobile lifting across stations.",
            "category": "Design & Fabrication",
            "image": "assets/images/cherry_picker.png",
            "github_link": "https://github.com/tchhajer/Engine-Cherry-Picker"
        },
        {
            "title": "Work Bench",
            "description": "Designed a modular and ergonomic steel workbench tailored for welding and mechanical assembly. Integrated storage and custom fixturing surfaces supported standardized work, 5S tool organization, and improved posture and productivity for operators.",
            "category": "Design & Fabrication",
            "image": "assets/images/workbench.png",
            "github_link": "https://github.com/tchhajer/Work-Bench"
        },
        {
            "title": "Semi-Autonomous Trolley",
            "description": "Designed and built a sensor-guided trolley using ultrasonic sensors and autonomy algorithms for path navigation. Engineered a custom 2-speed gearbox—uniquely implemented by our team—enabling seamless switching between high-torque and high-speed modes. This mechanical advantage allowed the trolley to adapt across competition challenges including hill climb, acceleration, speed, and autonomy tests, giving it a performance edge that no other team achieved.",
            "category": "Design & Fabrication",
            "image": "assets/images/trolley.png",
            "github_link": "https://github.com/tchhajer/Semi-Autonomus-Trolley"
        }, 
        {
            "title": "Overhead Structure Install",
            "description": "Developed a safe and efficient installation methodology for overhead crane structures supporting modular units. The process was OSHA-compliant, budget-conscious, and strategically designed to navigate existing overhead clearance and space limitations on the production floor.",
            "category": "Manufacturing Planning & Optimization",
            "image": "assets/images/ohc.png",
            "github_link": "https://github.com/tchhajer/Over-head-structure-install"
        },
        {
            "title": "Brucha Panel Installation",
            "description": "Created an efficient installation method for Brucha wall panels using a fork-mounted jib and suction lifting tools. The technique adhered to OSHA safety standards, optimized labor usage, and addressed spatial limitations in the facility—ultimately streamlining workflow and lowering installation costs.",
            "category": "Manufacturing Planning & Optimization",
            "image": "assets/images/brucha.png",
            "github_link": "https://github.com/tchhajer/Brucha-Panel-installation-method"
        },
        {
            "title": "Container Lift Solution",
            "description": "Engineered a cost-effective and OSHA-compliant solution for lifting large shipping containers using FEA to validate the structural integrity of the proposed design. The process minimized manual handling, improved safety, and was tailored to work within the facility's existing space constraints, reducing delays and assembly costs.",
            "category": "Manufacturing Planning & Optimization",
            "image": "assets/images/shuttlelift.png",
            "github_link": "https://github.com/tchhajer/Container-lift-solution"
        },
        {
            "title": "Mini Mate Install",
            "description": "Designed a clear and repeatable installation guide for integrating the Mini-Mate compact cooling system within a constrained workspace. The process improved worker safety, met OSHA guidelines, and minimized setup time, contributing to faster production and reduced labor costs.",
            "category": "Manufacturing Planning & Optimization",
            "image": "assets/images/mini_mate_install.png",
            "github_link": "https://github.com/tchhajer/Mini-Mate-Install"
        },
        {
            "title": "Cycle Time Worker Estimation",
            "description": "Developed an Excel-based tool to estimate workforce needs by analyzing task cycle times, pallet sizes, and daily throughput targets. The tool enabled more accurate labor planning and space allocation by correlating work duration with production schedules. It supported strategic SIOP initiatives, improving floor efficiency and reducing planning uncertainties.",
            "category": "Manufacturing Planning & Optimization",
            "image": "assets/images/cycle_time.png",
            "github_link": "https://github.com/tchhajer/Worker-estimation-using-cycle-time"
        },
        {
            "title": "Shelf Space Estimator",
            "description": "Designed an Excel-based tool to calculate total shelf and floor space required for storing Trinergy modules across different stages of production. Factored in pallet dimensions, number of working days per task, and throughput forecasts using SIOP data. This estimator improved layout planning and helped streamline storage logistics within tight facility constraints.",
            "category": "Manufacturing Planning & Optimization",
            "image": "assets/images/shelf_estimator.png",
            "github_link": "https://github.com/tchhajer/Floor-and-Shelf-Space-Estimator"
        },
        {
            "title": "Mobile Test Cart",
            "description": "Designed and fabricated a mobile testing cart to streamline the validation of modular electrical assemblies. The cart allowed testing to be conducted directly at storage locations, eliminating the need to transport heavy modules across the facility. This significantly reduced testing time, improved workflow efficiency, and lowered handling costs. Pre-programmed functionality made it operator-friendly and easy to deploy.",
            "category": "Design & Fabrication",
            "image": "assets/images/mobile_cart.jpg",
            "github_link": "https://github.com/tchhajer/Mobile-Test-cart"
        },
        {
            "title": "Robot Writer",
            "description": "Designed and built a compact robotic system capable of writing messages on a white board. Integrated servo motors and linkage-driven arms controlled via programmed coordinates to produce legible outputs. The project combined kinematic analysis, prototyping, and motion control, bridging mechanical design with entry-level automation.",
            "category": "Design & Fabrication",
            "image": "assets/images/robot.jpg",
            "github_link": "https://github.com/tchhajer/Robot-writer"
        },
        {
            "title": "Badger Ergonomist",
            "description": "Worked as part of a senior design team partnered with Doosan Bobcat to improve ergonomics and material flow on the manufacturing floor. Conducted site assessments and operator interviews to identify inefficiencies at the pound-out table and paint line unload station. Proposed and evaluated multiple solutions using CAD, SolidWorks animations, and Pugh matrices. Final recommendations were aligned with Lean principles and presented to company engineers and management.",
            "category": "Manufacturing Planning & Optimization",
            "image": "assets/images/badgerergo.png",
            "github_link": "https://github.com/tchhajer/Badger-ergonomist"
        },  
        {
            "title": "Drone Design Optimization",
            "description": "Designed a lightweight, extrudable drone frame optimized through FEA to meet strict deformation limits under multiple loading conditions. Balanced structural strength with material efficiency for manufacturability and performance.",
            "category": "FEA & Simulation",
            "image": "assets/images/drone.png",
            "github_link": "https://github.com/tchhajer/Drone-design-optimization"
        },   
        {
            "title": "Personal Projects",
            "description": "A variety of hands-on projects including laser-cut metal art pieces such as an F1 car, Bucky Badger, and family portraits. Also includes functional builds like a wood gasification stove, a custom-built coffee table through carpentry, and welded carabiner heart designs—demonstrating practical fabrication skills across metal and wood.",
            "category": "Design & Fabrication",
            "image": "assets/images/f1.png",
            "github_link": "https://github.com/tchhajer/Personal-Projects"
        },         
        {
            "title": "Manufacturing and floor plan optimization",
            "description": "Redesigned the facility layout of Tomahawk Metals using capacity analysis, flow relationship charts, and block diagrams to support 10-year growth projections. Assessed welding insourcing feasibility through sensitivity and payback analysis, and developed optimized floor plans prioritizing safety, efficiency, and sustainability.",
            "category": "Manufacturing Planning & Optimization",
            "image": "assets/images/ISYE_315.png",
            "github_link": "https://github.com/tchhajer/Manufacturing-and-floor-plan-optimization"
        },
        {
            "title": "Gear Box",
            "description": "Led the design and fatigue analysis of a two-stage reverted speed reducer for a go-kart application. This included gear sizing, material selection, force and stress analysis, and shaft and bearing design. Utilized SolidWorks for CAD modeling and EES for fatigue/life calculations. The final design balanced safety, performance, and manufacturability for high-shock racing conditions.",
            "category": "Design & Fabrication",
            "image": "assets/images/gearbox.png",
            "github_link": "https://github.com/tchhajer/Gear-box"
        },
        {
            "title": "Plug Plate Injection Molding",
            "description": "Engineered an injection-molded plug plate. The design was optimized using SolidWorks and validated via mold flow simulation and stress analysis to ensure manufacturability, minimal warpage, and longevity under load. Tooling geometry was refined to meet cost and cycle time targets.",
            "category": "FEA & Simulation",
            "image": "assets/images/pluginjection.png",
            "github_link": "https://github.com/tchhajer/Plug-Plate-injection-molding"
        },
        {
            "title": "Plastic Spoon Injection Molding",
            "description": "Designed and simulated a plastic spoon mold optimized for high-volume production. Analyzed gating, cooling, and ejection systems to ensure minimal warpage, efficient cycle times, and consistent quality.",
            "category": "FEA & Simulation",
            "image": "assets/images/spoon.png",
            "github_link": "https://github.com/tchhajer/Plastic-Spoon-Injection-Molding"
        },
        {
            "title": "Carabiner Test",
            "description": "Conducted extensive stress and fatigue testing on lightweight aluminum carabiner prototypes under varied environmental and geometric conditions. Simulated real-world loading scenarios across temperature extremes (hot and cold) and tested multiple size variants to evaluate strength retention, failure modes, and fatigue limits. Results informed design improvements for reliability in dynamic and high-load applications, particularly in safety-critical contexts.",
            "category": "Design & Fabrication",
            "image": "assets/images/carabiner.png",
            "github_link": "https://github.com/tchhajer/Carabiner-test"
        },

    ]

    if selected_category != "All":
        project_data = [proj for proj in project_data if proj["category"] == selected_category]

    # Add updated hover CSS
    st.markdown("""
        <style>
            .project-tile {
                position: relative;
                width: 100%;
                height: 260px;
                border-radius: 10px;
                overflow: hidden;
                box-shadow: 0 4px 8px rgba(0,0,0,0.1);
                margin-bottom: 10px;
                background-color: #f9f9f9;
                display: flex;
                align-items: center;
                justify-content: center;
            }
            .project-tile img {
                max-width: 100%;
                max-height: 100%;
                object-fit: contain;
                transition: 0.3s ease;
            }
            .overlay {
                position: absolute;
                top: 0;
                left: 0;
                height: 100%;
                width: 100%;
                background: rgba(0, 0, 0, 0.7);
                color: #fff;
                display: flex;
                align-items: center;
                justify-content: center;
                text-align: center;
                opacity: 0;
                padding: 10px;
                font-size: 14px;
                transition: opacity 0.3s ease;
            }
            .project-tile:hover .overlay {
                opacity: 1;
            }
            .project-tile:hover img {
                filter: brightness(40%);
            }
        </style>
    """, unsafe_allow_html=True)

    for i in range(0, len(project_data), 4):
        row_projects = project_data[i:i+4]
        cols = st.columns(4)

        for col, proj in zip(cols, row_projects):
            with col:
                if os.path.exists(proj["image"]):
                    img_data = base64.b64encode(open(proj["image"], "rb").read()).decode()
                    st.markdown(f"""
                        <div class="project-tile">
                            <a href="{proj['github_link']}" target="_blank">
                                <img src="data:image/jpeg;base64,{img_data}">
                                <div class="overlay">{proj['description']}</div>
                            </a>
                        </div>
                        <h4 style="text-align:center;">{proj['title']}</h4>
                    """, unsafe_allow_html=True)
                else:
                    st.warning(f"Image not found: {proj['image']}")

def resume():
    st.markdown("<h1 style='margin-bottom: 20px;'>Resume</h1>", unsafe_allow_html=True)

    resume_file_path = "assets/resume/resume.pdf"

    # Download button
    with open(resume_file_path, "rb") as f:
        st.download_button(
            label="📄 Download Resume",
            data=f,
            file_name="resume.pdf",
            mime="application/pdf"
        )

    # Display PDF inline
    with open(resume_file_path, "rb") as f:
        base64_pdf = base64.b64encode(f.read()).decode('utf-8')
        pdf_display = f'<iframe src="data:application/pdf;base64,{base64_pdf}" width="100%" height="800" type="application/pdf"></iframe>'
        st.markdown(pdf_display, unsafe_allow_html=True)

    # Download button
    with open(resume_file_path, "rb") as f:
        st.download_button(
            label="📄 Download Resume",
            data=f,
            file_name="resume.pdf",
            mime="application/pdf"
        )

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