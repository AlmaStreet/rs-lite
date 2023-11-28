import serial
from datetime import datetime
from random import random
from threading import Thread
from time import sleep, time


PATH = "/dev/cu."
PORT = "usbmodem14401"
serial_com = serial.Serial(PATH + PORT, 9600)
serial_com.timeout = 1

BYTE_C = b"c"  # misc
BYTE_Z = b"z"  # elven
BYTE_M = b"m"  # click


class Click:
    def __init__(self):
        self.stopped = True

        _time = time()
        self.click_time = _time
        self.elven_time = _time
        self.misc_time = _time

        self.misc_state = False
        self.elven_state = False
        self.click_state = False
        self.special = None

    def update_data(self, new_data):
        for key, value in new_data.items():
            setattr(self, key, value)

    def start(self):
        self.stopped = False
        t = Thread(target=self._run)
        t.start()

    def stop(self):
        self.stopped = True

    def _run(self):
        while not self.stopped:
            # press 'c'
            if self._valid_time(self.misc_time, self.misc_state):
                self._misc_action()

            # press 'z'
            if self._valid_time(self.elven_time, self.elven_state):
                self._elven_action()

            # click
            if self._valid_time(self.click_time, self.click_state):
                self._click_action()

        serial_com.close()

    def _valid_time(self, action_time, action_state):
        return time() > action_time and action_state

    def _get_current_time(self):
        return datetime.now().strftime("%H:%M:%S")

    def _get_new_time(self, random_time, constant_time):
        return time() + random() * random_time + constant_time

    def _print_current_action(self, text):
        now = self._get_current_time()
        print(f"[{now}] {text}")

    def _trigger_c_key(self):
        self._print_current_action(text="Use porter")
        serial_com.write(BYTE_C)

    def _trigger_z_key(self):
        self._print_current_action(text="Use elven")
        serial_com.write(BYTE_Z)

    def _trigger_click(self):
        self._print_current_action(text="Clicking")
        serial_com.write(BYTE_M)

    def _misc_action(self):
        self._trigger_c_key()

        self.misc_time = self._get_new_time(
            self.misc_time_random, self.misc_time_constant
        )
        sleep(random())

    def _elven_action(self):
        self._trigger_z_key()
        if self.special:
            self._elven_action_special()

        self.elven_time = self._get_new_time(
            self.elven_time_random, self.elven_time_constant
        )
        sleep(random())

    def _elven_action_special(self):
        if self.special == 4:
            sleep(2 + random() * 2)
            self._trigger_click()

            sleep(2 + random() * 2)
            self._trigger_click()

    def _click_action(self):
        self._trigger_click()
        if self.special:
            self._click_action_special()

        self.click_time = self._get_new_time(
            self.click_time_random, self.click_time_constant
        )
        sleep(random())

    def _click_action_special(self):
        if self.special == 1:
            sleep(1.5 + random() * 2)
            self._trigger_click()

            sleep(1.5 + random() * 2)
            self._trigger_z_key()

            sleep(1.5 + random() * 2)
            self._trigger_click()

        if self.special == 2:
            sleep(2 + random() * 2)
            self._trigger_click()

        if self.special == 3:
            sleep(5 + 1.5 * random())
            self._trigger_click()

            sleep(1.5 + random() * 2)
            self._trigger_z_key()

            sleep(1.5 + random() * 2)
            self._trigger_click()
