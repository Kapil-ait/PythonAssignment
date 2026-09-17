from pynput import keyboard

def press(key):

    print("Pressed:", key)

    if key == keyboard.Key.esc:
        return False

with keyboard.Listener(on_press=press) as listener:
    listener.join()