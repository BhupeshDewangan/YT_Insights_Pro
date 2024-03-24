import streamlit as st
from googleapiclient.discovery import build

api_key = st.secrets["api_key"]

# FIND THE API KEY HERE
# https://console.cloud.google.com/apis/credentials?project=yt-analysis-api

youtube = build('youtube', 'v3', developerKey=api_key)