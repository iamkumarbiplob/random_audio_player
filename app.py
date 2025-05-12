import random
import time
import threading
import os
import sys
from playsound import playsound


def get_audio_path():
    if getattr(sys, 'frozen', False):  # PyInstaller bundled
        base_path = sys._MEIPASS
    else:
        base_path = os.path.dirname(os.path.abspath(__file__))
    return os.path.join(base_path, "audio", "sound.mp3")


AUDIO_FILE = get_audio_path()


def play_audio_periodically():
    while True:
        delay = random.randint(0, 30 * 60)  # 0–1800 seconds
        print(f"wait: {delay}")
        time.sleep(delay)
        try:
            playsound(AUDIO_FILE)
        except Exception as e:
            print(f"Error playing sound: {e}")


def run():
    thread = threading.Thread(target=play_audio_periodically)
    thread.daemon = True
    thread.start()
    try:
        while True:
            time.sleep(60)
    except KeyboardInterrupt:
        print("Exiting...")


if __name__ == "__main__":
    run()
