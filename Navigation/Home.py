import streamlit as st
import requests
from streamlit_lottie import st_lottie
from streamlit_lottie import st_lottie_spinner
import time

# st.set_page_config(layout= "wide")

def load_lottieurl(url: str):
    r = requests.get(url)
    if r.status_code != 200:
        return None
    return r.json()


lottie_url1 = "https://lottie.host/daa9821a-0ef0-434b-a781-426f9c1592cd/JkRTFQ5sZE.json"

lottie_url2 = "https://lottie.host/2327ac9a-06a2-46c3-b869-1d8116cd7365/M3Du5uDPHm.json"

lottie_url3 = "https://lottie.host/feb49ed6-6f9e-454d-b722-52589c9321b8/fGLitA7eHO.json"

lottie_url4 = "https://lottie.host/daa9821a-0ef0-434b-a781-426f9c1592cd/JkRTFQ5sZE.json"

lottie_url5 = "https://lottie.host/d5b09c8d-beb7-49c5-8edb-7b2a87e0a116/6Xlw3TRR6K.json"


def home():
    col1, col2 = st.columns(2)

    with col1:
        # st.title("YT Insights Pro")
        # st.markdown('<h1 style="color: #ff4b4b;">YouTube Data API Analysis Project</h1>', unsafe_allow_html=True)
        st.markdown('<h1 style="color: #ff4b4b; text-align : center">YT Insights Pro</h1>', unsafe_allow_html=True)
        # st.write("")
        st.write("Welcome to our YouTube Data API Analysis Project! This project aims to analyze YouTube data to gain insights into trends, audience behavior, and more.")

    with col2:
        lottie_load = load_lottieurl(lottie_url2)
        st_lottie(lottie_load, key="hello", width=400, height=400)



    time.sleep(2)

    # Introduction
    st.header("Project Overview")
    st.write("In this project, we leverage the YouTube Data API to perform various analyses on YouTube data. Our goal is to provide users with valuable insights into the performance and trends of YouTube content. From analyzing video views and engagement metrics to identifying emerging trends and patterns, our platform offers a comprehensive suite of tools to empower users in making informed decisions about their YouTube channels and content strategies.")

    # Features
    st.header("Key Features")
    st.write("• In-depth analysis of video views, likes, comments, and other engagement metrics to gauge content performance.")
    st.write("• Identification of trends and patterns through data visualization and statistical analysis.")
    st.write("• Customizable analysis based on user input, allowing users to tailor insights according to their specific needs and goals.")

    # Benefits
    st.header("Benefits")
    st.write("Our project offers the following benefits:")
    st.write("• Helps content creators understand their audience better, leading to more targeted content creation and improved viewer satisfaction.")
    st.write("• Provides actionable insights to improve content strategy, optimize performance, and drive growth on the YouTube platform.")
    st.write("• Enables tracking of performance metrics over time, allowing users to monitor progress, measure success, and adapt strategies accordingly.")
