import pyautogui as pa
import time
import pickle
import sys
import argparse


def getPosition():
    print("Getting mouse position in 5 seconds")
    time.sleep(5)
    return pa.position()


if __name__ == '__main__':

    parser = argparse.ArgumentParser(description="click every x seconds a certain point of the screen")
    parser.add_argument("--set", action="store_true",
                        help="use --set option to set the position of the button to click")
    parser.add_argument("-t", type=int, default=90, help="use this option to set sleep time between clicks")
    args = parser.parse_args()

    try:
        with open("conf.pkl", "rb") as f:
            pos = pickle.load(f)

    except FileNotFoundError:
        if args.set:
            pos = getPosition()
            with open("conf.pkl", "wb") as f:
                pickle.dump(pos, f)
        else:
            print("you have to set position first!, use --set option")
            sys.exit(-1)

    print("button position set to: ", pos)

    clicks = 0
    secs = args.t
    while True:
        print(f"sleeping for {secs} seconds")
        time.sleep(secs-1)
        pa.moveTo(pos, duration=1)
        pa.click(pos)
        clicks += 1
        print(f"mouse clicked at position {pos}, total clicks: {clicks}")

