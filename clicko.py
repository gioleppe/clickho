import pyautogui as pa
import time
import argparse
from playsound import playsound

if __name__ == '__main__':

    parser = argparse.ArgumentParser(description="submits a task every x seconds (default 90)")
    parser.add_argument("-t", type=int, default=90, help="use this option to set sleep time between clicks")
    parser.add_argument("-s", action="store_true", default=False, help="use this flag to play a sound after each submission")
    args = parser.parse_args()

    pos = pa.locateCenterOnScreen('echo_save.png')

    print("button appears to be at: ", pos)

    clicks = 0
    secs = args.t
    while True:
        print(f"sleeping for {secs} seconds")
        time.sleep(secs - 1)
        pa.moveTo(pos, duration=1)
        pa.click(pos)
        clicks += 1
        print(f"mouse clicked at position {pos}, total clicks: {clicks}")
        playsound("quack.mp3")
