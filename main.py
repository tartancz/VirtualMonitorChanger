#!C:\Users\ruzicka\scripts\prepnutiObrazovek\venv\Scripts\python

from changer import Changer, Buttons
from time import sleep

if __name__ == '__main__':
    Changer(Buttons.RIGHT, 3, 5).start()
    while True:
        sleep(3600)