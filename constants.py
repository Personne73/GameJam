from pathlib import Path

FRAMERATE = 60 # Set fps
CASE_SIZE = 40 #pixels
IMG_PATH = str(Path.cwd()) + "/Sprites/"
WIDTH = 14
HEIGHT = 20
WINDOW_SIZE = (CASE_SIZE * WIDTH, CASE_SIZE * HEIGHT)
MOVE_STEPS = 8