import json
import os
import logging
from pathlib import Path

import spotipy
import spotipy.util as util

from telegram.ext import Updater, CommandHandler


logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.DEBUG
)

CONFIG = json.load(open(Path.cwd().joinpath('sp2tg/config.json'), 'r'))
SONG_INFO_PATH = Path.cwd().joinpath('sp2tg/songs.json')
DOWNLOAD_FOLDER = Path.cwd().joinpath('sp2tg/downloads')
CACHE_PATH = str(Path.cwd().joinpath(f"sp2tg/.cache-{CONFIG['SPOTIFY']['USER']}"))

if not os.path.exists(DOWNLOAD_FOLDER):
    os.makedirs(DOWNLOAD_FOLDER)

def show_tracks(context):
    token = util.prompt_for_user_token(
        CONFIG['SPOTIFY']['USER'],
        scope='user-library-read',
        client_id=CONFIG['SPOTIFY']['ID'],
        client_secret=CONFIG['SPOTIFY']['SECRET'],
        redirect_uri='http://localhost:8888',
        cache_path=CACHE_PATH
    )

    sp = spotipy.Spotify(auth=token)
    track = sp.current_user_saved_tracks(limit=1)['items'][0]['track']
    search_request = f"{track['name'] + ' - ' + track['artists'][0]['name']}"

    with open(SONG_INFO_PATH, 'r') as songsData:
        data = json.load(songsData)

    if data['RECENT_SONG'] == search_request:
        return
    data['RECENT_SONG'] = search_request

    with open(SONG_INFO_PATH, 'w') as songsData:
        json.dump(data, songsData)

    context.bot.send_message(
        chat_id=CONFIG['TELEGRAM']['CHANNEL_ID'],
        text=search_request
    )



updater = Updater(CONFIG['TELEGRAM']['KEY'], use_context=True)
jobs = updater.job_queue

fetch_songs = jobs.run_repeating(show_tracks, interval=60, first=0)

updater.start_polling()
