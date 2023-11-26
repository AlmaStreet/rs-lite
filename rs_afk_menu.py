import json
from clicker import Click
from datetime import datetime
from time import sleep
from tkinter import IntVar, Label, Radiobutton, Tk, W


def set_values():
    selection = str(var.get())

    text = "You selected the option " + str(selection)
    now = datetime.now().strftime("%H:%M:%S")

    if selection in data:
        print("[", now, f"] === {data[selection]['label']} ===")
        click.misc_state = eval(data[selection]["misc_state"])
        click.elven_state = eval(data[selection]["elven_state"])
        click.click_state = eval(data[selection]["click_state"])

        click.misc_time_random = data[selection]["misc_time_random"]
        click.misc_time_constant = data[selection]["misc_time_constant"]

        click.elven_time_random = data[selection]["elven_time_random"]
        click.elven_time_constant = data[selection]["elven_time_constant"]

        click.click_time_random = data[selection]["click_time_random"]
        click.click_time_constant = data[selection]["click_time_constant"]

        if "special" in data[selection]:
            click.special = data[selection]["special"]

        print(f"misc_state: {click.misc_state}")
        print(f"elven_state: {click.elven_state}")
        print(f"click_state: {click.click_state}")
        print()
        print(f"misc_time_random: {click.misc_time_random}")
        print(f"misc_time_constant: {click.misc_time_constant}")
        print()
        print(f"elven_time_random: {click.elven_time_random}")
        print(f"elven_time_constant: {click.elven_time_constant}")
        print()
        print(f"click_time_random: {click.click_time_random}")
        print(f"click_time_constant: {click.click_time_constant}")

        print(f"special: {click.special}")

        text_state = f"\nmisc: {click.misc_state}\nelven: {click.elven_state}\nclick: {click.click_state}\n== special: {click.special} =="
        label.config(text=text + text_state)


click = Click()
click.start()

f = open("data.json")
data = json.load(f)

root = Tk()
root.title("AFK Selection")
root.geometry("240x700")

var = IntVar(value=len(data))

index = 1
for element in data:
    radio_button = Radiobutton(
        root, text=data[element]["label"], variable=var, value=index, command=set_values
    )
    index += 1
    radio_button.pack(anchor=W)

label = Label(root)
label.pack()
root.update()

while True:
    sleep(0.1)
    root.update()

    # print(f"click.state: {click.state}")
    # print("fps: {}".format(1 / (time() - last_time)))

    # Press "q" to quit
    if 0xFF == ord("q"):
        click.stop()
        break
