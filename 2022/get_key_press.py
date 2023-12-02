#!/usr/bin/env python

from pynput import keyboard

# The currently active modifiers
current = set()

def on_press(key):
    current.add(key)
    if key == keyboard.Key.esc:
        listener.stop()

def on_release(key):
    try:
        current.remove(key)
    except KeyError:
        pass


with keyboard.Listener(on_press=on_press, on_release=on_release) as listener:
    listener.join()
