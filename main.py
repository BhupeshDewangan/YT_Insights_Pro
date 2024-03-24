import streamlit as st
import time
from streamlit_option_menu import option_menu


# Navigation --------------
from Navigation.Home import home
from Navigation.About_Page import About_Page
from Navigation.Creators import creators


# Importing from other pages -----------
from Python_Files.Creator_Search import *
from Python_Files.Channel_id import get_channel_id
from Python_Files.api_key import *

from Python_Files.Channel_Insights import basic_details
from Python_Files.Get_Functions import get_channel_stats, get_channel_info
from Python_Files.Get_Functions import get_video_details, get_video_ids, get_latest_videos
from Python_Files.Stats_Graphs import Statistics




def sidebar():
    with st.sidebar:
        selected = option_menu("Main Menu", ["Home", 'Creator Search', 'About'], 
            icons=['house-check', 'search-heart-fill', 'file-person-fill'], menu_icon="list", default_index=0,
            styles={
                # "icon": {"color": "white"}, 
                # "container": {"padding": "0!important", "background-color": "#fafafa"},
                # "nav-link": {"text-align": "left", "margin":"0px"},
                "nav-link-selected": {"background-color": "#ff4b4b"},
            })
        
    if selected == "Home":
        home()

    elif selected == "Creator Search":
        creators()

    elif selected == "About":
        About_Page()


def main():
    # Set page title and icon
    st.set_page_config(
        page_title="🎥 Youtube Creator Analyser ✨",
        page_icon="✨",
        layout="wide"
    )

    # with open('style.css') as f:
    #     st.markdown(f'<style>{f.read()}</style>', unsafe_allow_html=True)
    sidebar()


if __name__ == "__main__":
    main()
