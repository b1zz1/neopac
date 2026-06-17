import os
import sys

import config as cfg


def is_near_tile_center(pos):
    return 12 <= pos % cfg.TILE_SIZE <= 20


def resource_path(relative_path):
    """ Get absolute path to resource, works for dev and for PyInstaller """
    # Safely look for _MEIPASS without upsetting the linter
    base_path = getattr(sys, '_MEIPASS', os.path.abspath("."))
    return os.path.join(base_path, relative_path)
