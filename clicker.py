import serial
from datetime import datetime
from random import random
from threading import Thread
from time import sleep, time


serial_com = serial.Serial("/dev/cu.usbmodem14401", 9600)
serial_com.timeout = 1
# serial_com = None

# misc - c
# elven - z
# click - click


class Click:
    # constants
    stopped = True

    misc_time = None
    elven_time = None
    click_time = None

    misc_state = False
    elven_state = False
    click_state = False

    misc_time_random = 5
    misc_time_constant = 10

    elven_time_random = 5
    elven_time_constant = 10

    click_time_random = 5
    click_time_constant = 10

    special = None

    def __init__(self):
        self.click_time = time()
        self.elven_time = time()
        self.misc_time = time()

    def start(self):
        self.stopped = False
        t = Thread(target=self.run)
        t.start()

    def stop(self):
        self.stopped = True

    def misc_action(self):
        now = datetime.now().strftime("%H:%M:%S")
        print("[", now, "] Use porter")
        serial_com.write(b"c")

        self.misc_time = (
            time() + random() * self.misc_time_random + self.misc_time_constant
        )
        sleep(random())

    def elven_action(self):
        now = datetime.now().strftime("%H:%M:%S")
        print("[", now, "] Use elven")
        serial_com.write(b"z")

        if self.special == 4:
            sleep(2 + random() * 2)
            now = datetime.now().strftime("%H:%M:%S")
            print("[", now, "] Clicking")
            serial_com.write(b"m")

            sleep(2 + random() * 2)
            now = datetime.now().strftime("%H:%M:%S")
            print("[", now, "] Clicking")
            serial_com.write(b"m")

        self.elven_time = (
            time() + random() * self.elven_time_random + self.elven_time_constant
        )
        sleep(random())

    def click_action(self):
        now = datetime.now().strftime("%H:%M:%S")
        print("[", now, "] Clicking")

        if self.special == "agility":
            # eat mint cake
            if random() * 10 > 8.5:
                print("[", now, "] Eating mint cake")
                serial_com.write(b"z")
                sleep(1.5 + random() * 2)

        serial_com.write(b"m")

        if self.special == 1:
            sleep(1.5 + random() * 2)
            now = datetime.now().strftime("%H:%M:%S")
            print("[", now, "] Clicking")
            serial_com.write(b"m")

            sleep(1.5 + random() * 2)
            now = datetime.now().strftime("%H:%M:%S")
            print("[", now, "] Use elven")
            serial_com.write(b"z")

            sleep(1.5 + random() * 2)
            now = datetime.now().strftime("%H:%M:%S")
            print("[", now, "] Clicking")
            serial_com.write(b"m")

        if self.special == 2:
            sleep(2 + random() * 2)
            now = datetime.now().strftime("%H:%M:%S")
            print("[", now, "] Clicking")
            serial_com.write(b"m")

        if self.special == 3:
            sleep(5 + 1.5 * random())
            now = datetime.now().strftime("%H:%M:%S")
            print("[", now, "] Clicking")
            serial_com.write(b"m")

            sleep(1.5 + random() * 2)
            now = datetime.now().strftime("%H:%M:%S")
            print("[", now, "] Use elven")
            serial_com.write(b"z")

            sleep(1.5 + random() * 2)
            now = datetime.now().strftime("%H:%M:%S")
            print("[", now, "] Clicking")
            serial_com.write(b"m")

        self.click_time = (
            time() + random() * self.click_time_random + self.click_time_constant
        )
        sleep(random())

    def run(self):
        while not self.stopped:
            # press 'c'
            if time() > self.misc_time and self.misc_state:
                self.misc_action()

            # press 'z'
            if time() > self.elven_time and self.elven_state:
                self.elven_action()

            # click
            if time() > self.click_time and self.click_state:
                self.click_action()

        serial_com.close()
