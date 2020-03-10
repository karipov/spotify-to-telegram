import json
from pathlib import Path

CONFIG = json.load(Path.cwd().joinpath('config.json'))