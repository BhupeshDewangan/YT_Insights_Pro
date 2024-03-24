import streamlit as st
import requests
from Python_Files.api_key import *


@st.cache_data
# Function to fetch channel suggestions from YouTube Data API
def get_channel_suggestions(query):
    request = youtube.search().list(
        part="snippet",
        q=query,
        type="channel",
        maxResults=7
    )

    response = request.execute()

    suggestions = [item['snippet']['title'] for item in response.get('items', [])]
    
    # Return the list of channel titles
    return suggestions




# HIT AND TRY ------------------------------////////////
# def get_channel_suggestions(query):
#     url = f"https://www.googleapis.com/youtube/v3/search?key={api_key}&type=channel&part=snippet&q={query}&maxResults=15"
#     response = requests.get(url)
#     if response.status_code == 200:
#         data = response.json()
#         suggestions = [item['snippet']['title'] for item in data['items']]
#         return suggestions

#     else:
#         return []


