import streamlit as st
from datetime import datetime
from Python_Files.Get_Functions import *
from Python_Files.api_key import *
from Python_Files.Stats_Graphs import Statistics
import time

# OTHER FUNCTIONS -----------------------------------

def format_subscriber_count(count):
    c = int(count)
    if c >= 1000000:
        return f"{c / 1000000:.1f} Million"
    elif c >= 1000:
        return f"{c / 1000:.1f} K"
    else:
        return str(c)


def format_view_count(count):
    c = int(count)
    if c >= 10**5:
        lakh_c = c / 10**5
        return f"{lakh_c:.2f} Lakhs"
    else:
        return c


def top_6_videos(channel_id):
    latest_videos = get_latest_videos(channel_id)
    i = 0

    st.subheader("Here Is Some Latest YT Video From your Selected Channel")

    with st.spinner("Finding Youtube Videos"):
        time.sleep(2)

        for video in latest_videos:
            i = i + 1
            st1, st2 = st.columns(2)

            video_title = video['video_title']
            video_id = video['video_id']

            if(i % 2 == 0):
                st1.markdown(f"**Title:** {video_title}")

                st1.markdown(f'<iframe width="350" height="300" src="https://www.youtube.com/embed/{video_id}" frameborder="0" allowfullscreen></iframe>', unsafe_allow_html=True)
            
            else:
                st2.markdown(f"**Title:** {video_title}")

                st2.markdown(f'<iframe width="350" height="300" src="https://www.youtube.com/embed/{video_id}" frameborder="0" allowfullscreen></iframe>', unsafe_allow_html=True)


# MAIN FILE  ----------------------------

def basic_details(channel_id):

    channel_statistics = get_channel_stats(channel_id)
    channel_data = get_channel_info(channel_id)

    now = datetime.now()
    current_time = now.strftime("%Y-%m-%d %H:%M:%S")

    if channel_statistics:
        channel_name = channel_data.get('title')
        channel_description = channel_data.get('description')
        videoCount = channel_statistics.get('videoCount')
        subscriberCount = channel_statistics.get('subscriberCount')
        viewCount = channel_statistics.get('viewCount')

        # converted Values ------
        formatted_subscriber_count = format_subscriber_count(subscriberCount)
        formatted_view_count = format_view_count(viewCount)

        # st.markdown(f'<h5 style="color: white;">Channel Name: </h5> <h5 style="color: red;">{channel_name}</h5>', unsafe_allow_html=True)

        st.markdown(f'<h5 style="color: white;">Channel Name: {channel_name}</h5>', unsafe_allow_html=True)
        st.markdown(f'<h5 style="color: white;">Channel Description: {channel_description}</h5>', unsafe_allow_html=True)
        st.markdown(f'<h5 style="color: white;">Total Video Count Till [ {current_time} ] :- {videoCount}</h5>', unsafe_allow_html=True)
        st.markdown(f'<h5 style="color: white;">Total Numbers Of Subscriber in Channel Till [ {current_time} ] :- {formatted_subscriber_count}</h5>', unsafe_allow_html=True)
        st.markdown(f'<h5 style="color: white;">Total View Count Till [ {current_time} ] :- {formatted_view_count}</h5>', unsafe_allow_html=True)
        
        # st.markdown(f'<h5 style="color: white;">Total Numbers Of Subscriber in Channel Till {current_time}: {subscriberCount}")
        # st.markdown(f'<h5 style="color: white;">Total View Count Till {current_time}: {viewCount}")


        # NEXT FUNCTION CALL -------------------

        # Get the Playlist ID with MAX No. of Videos of Channel
        playlist_id = get_playlists(channel_id)

        # Get the Video IDs of Every Video of that Playlist
        video_ids = get_video_ids(playlist_id)

        # Show Stats of the videos of the Playlist
        Statistics(video_ids)

        # Latest 6 Videos
        top_6_videos(channel_id)

    else:
        st.header("Channel not found or statistics not available.")