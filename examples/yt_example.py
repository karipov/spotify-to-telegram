# -*- coding: utf-8 -*-

# Sample Python code for youtube.channels.list
# See instructions for running these code samples locally:
# https://developers.google.com/explorer-help/guides/code_samples#python

import os

import googleapiclient.discovery
import googleapiclient.errors
from pprint import pprint

def main():
    # Disable OAuthlib's HTTPS verification when running locally.
    # *DO NOT* leave this option enabled in production.

    api_service_name = "youtube"
    api_version = "v3"
    api_key = "AIzaSyDJPbRFaNt5aBzNqSp4t0k4VDOpM3RRhx8"

    # Get credentials and create an API client
    youtube = googleapiclient.discovery.build(
        api_service_name, api_version, developerKey=api_key)

    request = youtube.search().list(
        part="id,snippet,contentDetails",
        maxResults=2,
        q="Triumph"
    )
    response = request.execute()

    pprint(response)

if __name__ == "__main__":
    main()