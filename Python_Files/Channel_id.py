from Python_Files.api_key import *

def get_channel_id(channel_name):

    request = youtube.search().list(
        part="snippet",
        maxResults=1,
        q=channel_name,
        type="channel"
    )

    response = request.execute()

    if response['items']:
        channel_id = response['items'][0]['id']['channelId']
        return channel_id
    else:
        return None