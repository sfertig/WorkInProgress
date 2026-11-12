import os
from PyScene import Assets

_ASSET_DIR = os.path.join(os.path.dirname(__file__), "assets")

def load_assets():
    Assets.new_font('D35', None, 35)
    Assets.new_font('D_TITLE', None, 100)
    Assets.new_font('D45', None, 45)
