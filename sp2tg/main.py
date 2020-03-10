import json
import logging
from pathlib import Path

import spotipy
import spotipy.util as util

from telegram.ext import Updater, CommandHandler


logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.DEBUG
)

config = json.load(Path.cwd().joinpath('sp2tg/config.json'))

def show_tracks(update, context):
    print("call")
    token = util.prompt_for_user_token(
        config['SPOTIFY']['USER'],
        scope='user-library-read',
        client_id=config['SPOTIFY']['ID'],
        client_secret=config['SPOTIFY']['SECRET'],
        redirect_uri='http://localhost:8888'
    )
    print(token)

    sp = spotipy.Spotify(auth=token)
    track = sp.current_user_saved_tracks(limit=1)['items'][0]['track']

    update.message.reply_text(
        f"{track['name'] + ' - ' + track['artists'][0]['name']}"
    )


updater = Updater('1113497526:AAHCgx4jbV470cxa7OAMffEcKn-jdxC0sHE', use_context=True)

updater.dispatcher.add_handler(CommandHandler('start', show_tracks))

updater.start_polling()
