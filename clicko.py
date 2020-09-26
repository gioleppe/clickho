import pyautogui as pa
import time
import argparse


def getPosition():
    print("Getting mouse position in 5 seconds")
    time.sleep(5)
    return pa.position()


if __name__ == '__main__':

    parser = argparse.ArgumentParser(description="click every x seconds a certain point of the screen")
    parser.add_argument("-t", type=int, default=90, help="use this option to set sleep time between clicks")
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
