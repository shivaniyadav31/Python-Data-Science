#to run the server use command: streamlit run filename.py
#alternative option to run the server - python -m streamlit run filename.py
import streamlit as st

st.markdown('<h1 style="color:white; border: 12px solid pink; text-align:center">  Welcome to titanic dashboard </h1>',unsafe_allow_html=True)  #heading
st.set_page_config(page_title="Titanic Dashboard", layout="centered")

st.markdown('<div style="text-align: center; margin-top: 20px;"> <img src="assets\titanic-e1485201046467.jpg" alt="Titanic Dashboard" style="max-width: 70%; border-radius: 10px;"></div>',unsafe_allow_html=True)  #image

st.markdown('<div style="text-align: center; font-size: 18px; margin-top: 20px;"><p>Welcome aboard! This interactive dashboard allows you to explore the historic Titanic dataset.</p><p>Use the sidebar filters to refine your search and uncover fascinating insights about passengers, survival rates, fares, and much more.</p> </div>',unsafe_allow_html=True)

if st.button("📊 Go to Dashboard"):
    st.switch_page("pages/dashboard.py")  # Requires dashboard in pages/ folder