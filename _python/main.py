from PyScene import *
from load_assets import load_assets
Game.init(1920, 1080, 'GithubGameOff | PyScene Studio', [0, 0, 0], 60, True, True)
load_assets()
from data.main import main
main()
Game.Run()
