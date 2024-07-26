import streamlit as st
from page import home, about, detector

PAGES = {
    "Home": {"page": home, "title": "BreathEasy", "icon": "🏥"},
    "AI Pneumonia Screening": {"page": detector, "title": "Scan X-ray", "icon": "🔍"},
    "About Us": {"page": about, "title": "About Us", "icon": "👤"},
}

if 'current_page' not in st.session_state:
    st.session_state['current_page'] = 'Home'

def update_page_config(page_name):
    st.set_page_config (
        page_title=PAGES[page_name]['title'],
        page_icon=PAGES[page_name]['icon'],
        layout="wide",
        initial_sidebar_state="expanded",
        menu_items={
            'Get Help': 'mailto: tapankheni10304@gmail.com',
            'about': 'This is a web app that helps to detect pneumonia from X-ray images.'
        }
    )

update_page_config(st.session_state['current_page'])

with st.sidebar:
    st.write('## Navigation')
    selection = st.selectbox('Go to', list(PAGES.keys()), index=list(PAGES.keys()).index(st.session_state['current_page']))

if selection != st.session_state['current_page']:
    st.session_state['current_page'] = selection
    st.experimental_rerun()

page = PAGES[st.session_state['current_page']]['page']
page.run()
