import streamlit as st
from PIL import Image

def run():
    ## setting the title of th page
    st.title("BreathEasy: Rapid Pneumonia Screening Tool 🩻")

    ## setting sidebar
    with st.sidebar:
        st.write('\n')
        st.write('\n')
        st.write('\n')
        st.markdown("""
        <div style="padding: 10px; border: 2px solid #ffffff; border-radius: 15px; background-color: #0E1117; color: #ffffff; width: fit-content; justify-content: center;">
            Enhance patient care with AI-powered pneumonia detection 🫁 by identifying potential cases early 🔍 and enabling prompt treatment.
        </div>
        """, unsafe_allow_html=True)

        st.write('\n')
        st.write('\n')
        st.write('\n')
        st.markdown("""
        <div style="padding: 10px; border: 2px solid #ffffff; border-radius: 15px; background-color: #0E1117; color: #ffffff; width: fit-content; justify-content: center;">
            ⚠️<b>Disclaimer:</b><br></br>Professional medical advice is must. <br></br>This tool complements, not replaces, your doctor's expertise. <br></br>For any health concerns, consult your doctor.
        </div>
        """, unsafe_allow_html=True)

    st.header("What is Pneumonia? 🤔", divider="rainbow")

    st.write("""
    Pneumonia is an infection caused by bacteria, viruses, or fungi. It leads to inflammation in the air sacs of one or both lungs. 
    These sacs, called alveoli, fill with fluid or pus, making it difficult to breathe.
    """)

    logo = Image.open("static/logo.png")
    left_column, center_column, right_column = st.columns(3)

    with center_column:
        st.write('\n')
        st.image(logo)

    st.write("\n")
    st.write("""
    - Both viral and bacterial pneumonia is contagious. This means they can spread from person to person through inhalation of airborne droplets from a sneeze or cough.
    - You can also get these types of pneumonia by coming into contact with surfaces or objects that are contaminated with pneumonia-causing bacteria or viruses.
    - You can contract fungal pneumonia from the environment. It does not spread from person to person.
    """)

    st.subheader("Bussiness Context")
    st.write("""
    The goal of AI-assisted pneumonia detection is to help healthcare providers and hospitals improve patient outcomes and optimize resource allocation. 
    By identifying potential pneumonia cases early and accurately, medical professionals can initiate timely interventions and provide targeted care.
    """)

    st.header("How it works", divider="rainbow")
    st.write("""
    The CNN is trained on a large dataset of chest X-rays, enabling it to:

    - Identify potential pneumonia cases from medical imaging.

    This AI-enabled solution has the potential to:
    - Reduce the time needed for pneumonia diagnosis.
    - Improve the accuracy of pneumonia detection.
    - Enhance the overall quality of patient care in respiratory medicine.
    """)

    st.header("Who Can Benefit from it?", divider="rainbow")
    st.write("""
    - Hospitals.
    - Radiology departments.
    - Urgent care centers.
    - Pulmonology clinics.
    - Medical Research Institutes.
    """)

    st.write("""
    Stay tuned for updates as we continue to refine and enhance this innovative AI solution for more lung related abnormalities.
    """)

    
         