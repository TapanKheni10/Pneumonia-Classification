from PneumoniaDetection.prediction_component.predict import PredictionPipeline
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
                                     help="upload the image file over here for which you want to detect the pneumonia")
    
    if uploaded_file is not None:
        image = Image.open(uploaded_file)

        obj = PredictionPipeline(image)
        prediction = obj.predict()

        left_column, right_column = st.columns(2)
        with left_column:
            st.image(image, caption="Given X-Ray:", use_column_width=True)

        with right_column:
            if prediction >= 0.8:
                image = Image.open('static/issue.jpeg')
                st.image(image, use_column_width=True)
                st.error("🔴 Pneumonia detected in the X-ray. Please consult a doctor. 👨🏻‍⚕️")
            else:
                image = Image.open('static/success.jpeg')
                st.image(image, use_column_width=True)
                st.success("🟢 No pneumonia detected in the X-ray. Stay healthy! 🌟")
    
    