import streamlit as st


def About_Page():
    st.markdown('<h3 style= "text-align: center">Welcome to</h3>', unsafe_allow_html=True)
    st.markdown('<h1 style="color: #ff4b4b; text-align : center">YT Insights Pro</h1>', unsafe_allow_html=True)

    st.write('A basic dynamic site designed to provide comprehensive analysis and insights from YouTube channels. I am trying to delivering a simple user experiences and valuable data-driven insights to content creators, marketers, and analysts alike.')

    st.header("Mission")
    st.write("At YT Insights Pro, My mission is to empower YouTube creators with actionable insights to watch their channel performance and audience engagement. I strive to achieve this by leveraging advanced analytics and basic-edge technologies.")

    st.header("Development Tech and Tools")
    st.markdown("""
    - Python and Streamlit
    - Youtube Data API From Google Cloud
    - Google Colab for Analysis and Dashboarding
    """)

    st.header("Contact Me")

    st.write("I value your feedback and are always eager to hear from our users. If you have any questions, suggestions, or encounter any issues while using YT Insights Pro, please don't hesitate to reach out to us. You can contact us via:")

    st.markdown("""
    - Email : bhupeshdewangan2003@gmail.com
    - Phone : 8319341550
    - Linkedin : https://www.linkedin.com/in/bhupesh-dewangan-7121851ba/
    - Github : https://github.com/BhupeshDewangan
    """)


    st.error("If you come across any technical issues or bugs within the app, please report or send a message to me. Your input helps us improve YT Insights Pro and deliver a seamless experience for all users.")

    st.write("---")
    st.success("Thank you for choosing [YT Insights Pro]. We appreciate your support and look forward to serving you better in the future.")
