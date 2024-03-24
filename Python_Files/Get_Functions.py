import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import calendar

from streamlit_option_menu import option_menu
from Python_Files.api_key import *

# FUNCTIONS -----------------------------


# 1 --------------
def get_channel_info(channel_id):
    request = youtube.channels().list(
        part='snippet',
        id=channel_id
    )
    response = request.execute()
    if response['items']:
        channel_info = response['items'][0]['snippet']
        return channel_info
    else:
        return None


# 2 --------------
def get_channel_stats(channel_id):
    request = youtube.channels().list(
        part='statistics, snippet, contentDetails',
        id=channel_id
    )
    response = request.execute()

    if response['items']:
        statistics = response['items'][0]['statistics']
        return statistics
    else:
        return None


# 3 ---------------------------
def get_playlists(channel_id):
    request = youtube.playlists().list(
        part="snippet,contentDetails",
        channelId = channel_id,
        maxResults=25
    )

    response = request.execute()

    max_video_count = 0
    max_video_playlist = None
    max_video_playlist_id = None

    for playlist in response['items']:
        title = playlist['snippet']['title']
        playlist_id = playlist['id']
        video_count = int(playlist['contentDetails']['itemCount'])

        if video_count > max_video_count:
            max_video_count = video_count
            max_video_playlist = title
            max_video_playlist_id = playlist_id

    st.write("---")
    st.markdown(f'<h5 style="color: white;">Playlist with the highest number of videos : {max_video_playlist}</h5>', unsafe_allow_html=True)
    # st.write(max_video_playlist)
    st.markdown(f'<h5 style="color: white;">Number of videos in the playlist : {max_video_count}</h5>', unsafe_allow_html=True)
    # st.write(max_video_count)

    return max_video_playlist_id


# 4 -------------------------
def get_video_ids(playlist_id):

    request = youtube.playlistItems().list(
          part="contentDetails",
          playlistId=playlist_id,
          maxResults = 50
        )

    response = request.execute()

    video_ids = []

    for i in range(len(response['items'])):
      video_ids.append(response['items'][i]['contentDetails']['videoId'])

    next_page_token = response.get('nextPageToken')
    more_pages = True

    while more_pages:
      if next_page_token is None:
        more_pages = False

      else:
        request = youtube.playlistItems().list(
          part="contentDetails",
          playlistId=playlist_id,
          maxResults = 50,
          pageToken = next_page_token
        )
        response = request.execute()

        for i in range(len(response['items'])):
          video_ids.append(response['items'][i]['contentDetails']['videoId'])

        next_page_token = response.get('nextPageToken')

    return video_ids
    # return response

# 5 -----------------------------------
def get_video_details(video_ids):

    all_video_stats = []

    for i in range(0, len(video_ids), 50):
        request = youtube.videos().list(
                part="snippet,statistics",
                id=','.join(video_ids[i:i+50])
        )

        response = request.execute()

        for video in response['items']:
            video_stats = dict(Title = video['snippet']['title'],
                            publish_date = video['snippet']['publishedAt'],
                            viewCount = video['statistics']['viewCount'],
                            likeCount = video['statistics']['likeCount'],
                            commentCount = video['statistics']['commentCount'],
                            )

            all_video_stats.append(video_stats)

    return all_video_stats


# 6 ---------------------------
# GET THE LATEST VIDEOS

def get_latest_videos(channel_id):
    # Call the search.list method of the YouTube Data API
    request = youtube.search().list(
        part="snippet",
        channelId=channel_id,
        maxResults=6,
        order="date"  # Order by upload date
    )
    response = request.execute()

    # Extract video information from the response
    videos = []
    for item in response['items']:
        if item['id']['kind'] == 'youtube#video':
            video_id = item['id']['videoId']
            video_title = item['snippet']['title']
            videos.append({'video_id': video_id, 'video_title': video_title})

    return videos



# 7 ---------------------------
def DataFrame():
    video_details = get_video_details(video_ids)
    video_df = pd.DataFrame(video_details)
    st.dataframe(video_df, width=1500, height=300)

