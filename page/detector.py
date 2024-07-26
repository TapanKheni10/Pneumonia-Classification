import streamlit as st
from PIL import Image

def run():
    with st.sidebar:
        st.write('\n')
        st.write('\n')
        st.write('\n')
        st.markdown("""
        <div style="padding: 10px; border: 2px solid #ffffff; border-radius: 15px; background-color: #0E1117; color: #ffffff; width: fit-content; justify-content: center;">
            🫁 Identify potential pneumonia cases with our advanced AI-assisted X-ray analysis.
        </div>
        """, unsafe_allow_html=True)

    st.header("Chest X-ray Assessment", divider="rainbow")

    st.write("""
        Please enter the X-ray image in valid format (.jpeg, .png, .jpg), and the system will automatically detect the presence of pneumonia.
    """)

    uploaded_file = st.file_uploader(label="**Upload the File**", type=['.jpeg', '.png', '.jpg'], 
                                     help="upload the file of data over here for which you want to make prediction")
    
    