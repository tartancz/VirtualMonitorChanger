import time
from enum import Enum

from pyvda import VirtualDesktop, get_virtual_desktops
import mouse

from mouse._mouse_event import LEFT, RIGHT, MIDDLE, UP

class Buttons(Enum):
    LEFT = LEFT
    RIGHT = RIGHT
    MIDDLE = MIDDLE

class Changer:
    _events: list[float] = []
    _event = None
    def __init__(self, button: Buttons, number_of_clicks: int, delay_of_clicks: float):
        self.button = button
        self.number_of_clicks = number_of_clicks
        self.delay_of_clicks = delay_of_clicks

    @staticmethod
    def change_monitor():
        list_desktop = get_virtual_desktops()
        if len(list_desktop) != 2:
            return
        current_window = VirtualDesktop.current()
        for dsk in list_desktop:
            if current_window.id != dsk.id:
                dsk.go()

    def clicked(self):
        self._events.append(time.time())
        if len(self._events) < self.number_of_clicks:
            return
        oldests_click = self._events.pop(0)
        if time.time() - oldests_click < self.delay_of_clicks:
            self.change_monitor()
            self._events.clear()

    def start(self):
       self._event = mouse.on_button(self.clicked,() , [self.button.value], [UP])
