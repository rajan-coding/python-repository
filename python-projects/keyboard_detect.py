from pynput import keyboard

def sample():
    print("dfdffdf")

def on(key):
   print(f"key pressed {key}")

def off(key):
    print(f"key released {key}")

with keyboard.Listener(on_press=on, on_release=off) as listener:
    listener.join()
    sample()

