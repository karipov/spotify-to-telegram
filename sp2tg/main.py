import sys
import spotipy
import spotipy.util as util

from telegram.ext import Updater, CommandHandler
import logging

logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                     level=logging.DEBUG)

USERNAME = 'komron_aripov'

def show_tracks(update, context):
    print("call")
    token = util.prompt_for_user_token(
        USERNAME,
        scope='user-library-read',
        client_id='a2d67890944043a89bc49b968674464a',
        client_secret='8964fab6a6ee48468946d7c3be674e5e',
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
