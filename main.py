#!C:\Users\ruzicka\scripts\prepnutiObrazovek\venv\Scripts\python

import time

from pyvda import VirtualDesktop, get_virtual_desktops
import mouse

def ChangeDesktop():
    list_desktop = get_virtual_desktops()
    if len(list_desktop) != 2:
        return
    current_window = VirtualDesktop.current()
    for dsk in list_desktop:
        if current_window.id != dsk.id:
            dsk.go()

clicked = 0
swapped = 0
def get_events():
    global clicked, swapped
    act_time = time.time()
    if act_time - clicked < 1 and act_time - swapped > 1:
        swapped = act_time
        ChangeDesktop()
    else:
        clicked = act_time


if __name__ == '__main__':
    mouse.on_middle_click(get_events)
    while True:
        time.sleep(3000)