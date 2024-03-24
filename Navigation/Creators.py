import streamlit as st

# Importing from other pages -----------
from Python_Files.Creator_Search import *
from Python_Files.Channel_id import get_channel_id
from Python_Files.api_key import *

from Python_Files.Channel_Insights import basic_details
from Python_Files.Creator_Search import get_channel_suggestions
from Python_Files.Get_Functions import get_channel_stats, get_channel_info
from Python_Files.Get_Functions import get_video_details, get_video_ids, get_latest_videos
from Python_Files.Stats_Graphs import Statistics



def creators():
    st.markdown('<h1 style="color: #ff4b4b; text-align : center">YT Insights Pro</h1>', unsafe_allow_html=True)
    st.markdown('<h4 style="color: white;">Discover your favorite youtube channel unique insights with Charts and Graphs from my personal YouTube Analytics Site.</h4>', unsafe_allow_html=True)

    channel_name = st.text_input("Enter YouTube Channel Name:", key="channel_name")

    # Fetch and display autocomplete suggestions as the user types
    if channel_name:
        suggestions = get_channel_suggestions(channel_name)
        st.subheader("Suggestions:")
        selected_channel = st.selectbox("Select a channel:", options=suggestions)

        if st.button("Submit"):
            st.write("You selected:", selected_channel)

            channel_id = get_channel_id(selected_channel)   

            if channel_id:
                # with st.spinner('PROCESSING..........'):
                #     time.sleep(2)
                st.success(f"Channel ID found: {channel_id}")
                
                basic_details(channel_id)

            else:
                st.write("Channel not found. Please try again with a different name.")
