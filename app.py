import streamlit as st
from PIL import Image
import json

# Load image
image = Image.open("profile.jpg")

# Load projects
with open("projects.json") as f:
    projects = json.load(f)

# Sidebar
st.sidebar.image(image, width=150)
st.sidebar.title("Amit Kasar")
st.sidebar.markdown("AI/ML Enthusiast | Web Dev | Cybersecurity")

# Tabs
tab1, tab2, tab3, tab4 = st.tabs(["🧑‍💼 About", "🛠️ Skills", "📂 Projects", "📞 Contact"])

# About
with tab1:
    st.header("About Me")
    st.write("""
    I'm currently pursuing B.E. in Artificial Intelligence and Machine Learning.  
    Passionate about building intelligent systems and solving real-world problems using AI, ML, and Web Tech.
    """)

# Skills
with tab2:
    st.header("Skills")
    cols = st.columns(3)
    skills = ["Python", "Flask", "Streamlit", "Machine Learning", "HTML/CSS", "JavaScript", "Arduino", "Burp Suite", "Git"]
    for i, skill in enumerate(skills):
        cols[i % 3].markdown(f"✅ {skill}")

# Projects
with tab3:
    st.header("Projects")
    for project in projects:
        st.subheader(project["title"])
        st.write(project["description"])
        if project.get("link"):
            st.markdown(f"[View Project]({project['link']})")

# Contact
email = "amitcollege57.com"
linkedin = "https://www.linkedin.com/in/amit-kasar-0ba8502b4?utm_source=share&utm_campaign=share_via&utm_content=profile&utm_medium=android_app"
github = "https://github.com/Amit-Kasar57"

with tab4:
    st.header("Get in Touch")
    st.markdown(f"📧 [Email](mailto:{email})")
    st.markdown(f"🔗 [LinkedIn]({linkedin})")
    st.markdown(f"🐙 [GitHub]({github})")
