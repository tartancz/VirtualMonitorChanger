#!C:\Users\ruzicka\scripts\prepnutiObrazovek\venv\Scripts\python

from changer import Changer, Buttons
from time import sleep

if __name__ == '__main__':
    Changer(Buttons.RIGHT, 3, 0.5).start()
    Changer(Buttons.MIDDLE, 2, 1).start()
    while True:
        sleep(3600)