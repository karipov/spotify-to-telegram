from . import CONFIG

class SpotifyExtractor:
    def __init__(oauth):
        self.scope = CONFIG['SPOTIFY']['SCOPE']
        self.id = CONFIG['SPOTIFY']['ID']
        self.secret = CONFIG['SPOTIFY']['SECRET']