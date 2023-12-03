import serial
from datetime import datetime
from random import random
from threading import Thread
from time import sleep, time


PATH = "/dev/cu."
PORT_TYPE = "usbmodem"
PORT = "2301"
BYTE_C = b"c"  # misc
BYTE_Z = b"z"  # elven
BYTE_M = b"m"  # click


class Click:
    def __init__(self):
        self.serial_com = serial.Serial(PATH + PORT_TYPE + PORT, 9600)
        self.serial_com.timeout = 1

        self.thread = None
        self.stopped = True
        self._initialize_times()
        self._initialize_states()

    def _initialize_times(self):
        current_time = time()
        self.click_time = current_time
        self.elven_time = current_time
        self.misc_time = current_time

    def _initialize_states(self):
        self.misc_state = False
        self.elven_state = False
        self.click_state = False
        self.special = None

    def start(self):
        if self.thread and self.thread.is_alive():
            print("A clicker thread is already running.")
            return
        self.stopped = False
        self.thread = Thread(target=self._run)
        self.thread.start()

    def stop(self):
        self.stopped = True
        if self.thread:
            self.thread.join()
            self.thread = None

    def _run(self):
        try:
            while not self.stopped:
                self._execute_actions()
        finally:
            self.serial_com.close()

    def _execute_actions(self):
        if self._valid_time(self.misc_time, self.misc_state):
            self._misc_action()

        if self._valid_time(self.elven_time, self.elven_state):
            self._elven_action()

        if self._valid_time(self.click_time, self.click_state):
            self._click_action()

    def update_data(self, new_data):
        allowed_keys = {
            "misc_state",
            "elven_state",
            "click_state",
            "special",
            "misc_time_random",
            "misc_time_constant",
            "elven_time_random",
            "elven_time_constant",
            "click_time_random",
            "click_time_constant",
        }

        for key, value in new_data.items():
            if key in allowed_keys:
                setattr(self, key, value)

    def _valid_time(self, action_time, action_state):
        return time() > action_time and action_state

    def _get_current_time(self):
        return datetime.now().strftime("%H:%M:%S")

    def _get_new_time(self, random_time, constant_time):
        return time() + random() * random_time + constant_time

    def _print_current_action(self, text):
        print(f"[{self._get_current_time()}] {text}")

    def _trigger_key(self, byte_key):
        try:
            self.serial_com.write(byte_key)
            self.serial_com.flush()
        except serial.SerialException as e:
            print(f"SerialException encountered: {e}")
            self._handle_serial_error()

    def _handle_serial_error(self):
        try:
            self.serial_com.close()
            sleep(1)
            self.serial_com.open()
        except serial.SerialException as e:
            print(f"Failed to reopen serial connection: {e}")
            self.stop()

    def _misc_action(self):
        self._trigger_key(BYTE_C)
        self._print_current_action(text="Use porter")

        self.misc_time = self._get_new_time(
            self.misc_time_random, self.misc_time_constant
        )
        sleep(random())

    def _elven_action(self):
        self._trigger_key(BYTE_Z)
        self._print_current_action(text="Use elven")

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
        self._trigger_key(BYTE_M)
        self._print_current_action(text="Clicking")

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
