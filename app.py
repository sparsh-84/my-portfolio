from pathlib import Path
import json
import streamlit as st
from streamlit_option_menu import option_menu
from PIL import Image
import requests
from streamlit_lottie import st_lottie
from typing_extensions import Literal


# --- PATH SETTINGS ---
current_dir = Path(__file__).parent if "__file__" in locals() else Path.cwd()
css_file = current_dir / "styles" / "main.css"
# resume_file = current_dir / "assets" / "CV.pdf"
profile_pic = current_dir / "assets" / "profile-pic.png"

PAGE_TITLE = "Portfolio | Sparsh Goel"
PAGE_ICON = ":wave:"
st.set_page_config(page_title=PAGE_TITLE, page_icon=PAGE_ICON, layout="wide")

def loadlottiefiles(filepath: str):
    with open(filepath, "r") as f:
        return json.load(f)

lottie_hello = loadlottiefiles("assets/animation_lltyzttt.json")
lottie_social = loadlottiefiles("assets/social_networks.json")
lottie_contact = loadlottiefiles("assets/contact_me.json")

NAME = "Sparsh Goel"
DESCRIPTION = """
            Crafting a Data-Driven Future: Journey of a Future Data Analyst, 
            Hello there! I'm Sparsh, a CSE senior at JIIT. Navigating the realms of data, 
            I am on a mission to decode information and drive informed decisions. 
            Step into my world where numbers come alive and stories are told through data analysis.
            """
EMAIL = "goelsparsh01@gmail.com"
SOCIAL_MEDIA = {
    "LinkedIn": "https://www.linkedin.com/in/sparsh84/",
    "GitHub": "https://github.com/sparsh-84",
    "Instagram": "https://www.instagram.com/sparsh_84/",
}

# --- LOAD CSS, PDF & PROFIL PIC ---
with open(css_file) as f:
    st.markdown("<style>{}</style>".format(f.read()), unsafe_allow_html=True)
# with open(resume_file, "rb") as pdf_file:
#     PDFbyte = pdf_file.read()
profile_pic = Image.open(profile_pic)

# st.markdown(
#     """
#     <style>
#         # div[data-testid="column"]:nth-of-type(1)
#         # {
#         #     border:10px solid white;
#         # }

#         div[data-testid="column"]:nth-of-type(3)
#         {
#             text-align: end;
#         } 
#     </style>
#     """,unsafe_allow_html=True
# )

# --- HERO SECTION ---
# col1, col2, col3 = st.columns(3, gap="small")
col1, col2 = st.columns((1,2))
with col1:
    st.write("##")
    st.write("##")
    st.image(profile_pic, width=280)

with col2:
    st.subheader("Hey Guys :wave:")
    st.title("I am Sparsh Goel")
    # st.title(NAME)
    st.write(DESCRIPTION)
    st.download_button(
        label=" 📄 Download Resume",
        # data=PDFbyte,
        # file_name=pdf_file.name,
        mime="application/octet-stream",
    )
    st.write("📫", EMAIL)
    st.subheader("**Connect with Me**")
    # st.write('----')
    cols = st.columns(len(SOCIAL_MEDIA))
    for index, (platform, link) in enumerate(SOCIAL_MEDIA.items()):
        cols[index].write(f":bust_in_silhouette: [{platform}]({link})")
    # st.write('----')    

        

# with col3:
#     st_lottie(lottie_social, height= 305)
#     st.write("Connect with Me")
#     st.write('----')

# with col3:
#     cols = st.columns(len(SOCIAL_MEDIA))
#     for index, (platform, link) in enumerate(SOCIAL_MEDIA.items()):
#         cols[index].write(f"[{platform}]({link})")
#     st.write('----')


# --- SOCIAL LINKS ---
# st.write('\n')
# cols = st.columns(len(SOCIAL_MEDIA))
# for index, (platform, link) in enumerate(SOCIAL_MEDIA.items()):
#     cols[index].write(f"[{platform}]({link})")


with st.container():
    selected = option_menu( 
        menu_title=None,
        options= ['About', 'Projects', 'Work History', 'Contact Me',],
        icons=['person', 'code-slash', 'play', 'chat-left-text-fill'],
        orientation= 'horizontal'
    )

if selected == 'About':
    with st.container(): 
        col1, col2 = st.columns(2)
        with col1:
            st.write("##")
            st.subheader("I am Sparsh Goel")
            st.title("UnderGrad at Jaypee Institute of Information Technology")
        with col2:
            st_lottie(lottie_hello, height = 280)

    st.write('----')

    with st.container():
        col3,col4 = st.columns(2) 
        with col3:
            st.subheader(""" 
            Education

            -   :mortar_board: Undergraduate (UG) - 2020-24
                - Bachelor of Technology in Computer Science & Engineering (CSE) 
                - Jaypee Institute of Information Technology, Noida
                - 4th year (7th sem)
                - Grade: 7 CGPA
                #
            -   :school_satchel: XIIth - 2019-20
                - Delhi Public School, Greater Noida
                - PCM 
                - Grade: 94.25%
                #
            -   :school_satchel: Xth - 2017-18
                - Delhi Public School, Greater Noida
                - Grade: 90.6%
        """)
    
        with col4:
            st.subheader("""
            Hard Skills
            - 👩‍💻 Programming: Python (Numpy, Pandas), Django, MySQL
            - 📊 Data Visulization: MS Excel, MS PowerPoint, MS Word, Plotly, Seaborn
            - 🗄️ Databases: MySQL, MongoDB
            """)

        with col4:
            st.subheader("""
            Soft Skills
            - ✔️ Ability to Multitask
            - 📚 Communication Skill
            - ✔️ Problem Solving
            - 📚 Analytical Skill
            """)

# --- Projects & Accomplishments ---

if selected == 'Projects':
    with st.container(): 
        st.header("Projects & Accomplishments")
        st.write("---")
        st.write("""🏆 - Stock and Crypto-Currency Price Analysis with Python (5th semester, Minor):""")
        st.caption("""This online application will display stock and cryptocurrency prices (web scrapped) and visually appealing graphs to learn about price movements.""")
        st.write("[Visit Github Repo](https://github.com/sparsh-84/stock-and-crypto-analysis-dashboard)")
        st.write("##")
        st.write("""🏆 - YouTube Content Moderation (6th semester, Minor):""")
        st.caption("""The user will learn more about the subjects covered in the YouTube video, and it also categorises the content under several subheadings. 
    This can be used to check the videos and find any sensitive information they may contain.""")
        st.write("[Visit Github Repo](https://github.com/sparsh-84/youtube-content-moderation)")

# # --- WORK HISTORY ---        
if selected == 'Work History':
    # --- JOB 1
    st.write("[🚧 **Full Stack Developer Internship | Kredmint Technologies Pvt. Ltd.**](https://www.kredmint.com/)")
    st.write("06/2023 - 07/2023")
    st.write(
    """
    Over two months, the project involved:
    - ► Setup & Learning: Establishing a virtual environment, mastering Django fundamentals, integrating a simple and appealing UI
    - ► Advanced Development: Bridging Django and MongoDB with djongo, implementing CRUD operations for data manipulation and ensuring functionality through extensive testing.
    - ► Deployment & Documentation: Preparing the project for deployment, documenting setup and usage, and deploying the admin panel on a test server for final checks.
    """
    )

if selected == 'Contact Me':
    st.header(":mailbox: Get In Touch With Me")
    st.write("##")
    st.write("##")

    contact_form = """
    <form action="https://formsubmit.co/goelsparsh01@gmail.com" method="POST">
        <input type="hidden" name="_captcha" value="false">
        <input type="text" name="name" placeholder="Your name" required>
        <input type="email" name="email" placeholder="Your email" required>
        <textarea name="message" placeholder="Your message here"></textarea>
        <button type="submit">Send</button>
    </form>
    """
    left_col, right_col = st.columns((2,1))
    with left_col:
        st.markdown(contact_form, unsafe_allow_html= True)
        # Use Local CSS File
        def local_css(file_name):
            with open(file_name) as f:
                st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)
    local_css("styles/form_style.css")

    with right_col:
        st_lottie(lottie_contact, height=280)

