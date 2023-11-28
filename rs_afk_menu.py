import json
from clicker import Click
from datetime import datetime
from time import sleep
from tkinter import IntVar, Label, Radiobutton, Tk, W


def initialize_ui():
    tk = Tk()
    tk.title("AFK Selection")
    tk.geometry("240x720")

    return tk


def set_values():
    selection = str(var.get())
    text = "You selected the option " + str(selection)
    now = datetime.now().strftime("%H:%M:%S")

    if selection in data:
        click.update_data(data[selection])

        text_state = f"\nmisc: {click.misc_state}\nelven: {click.elven_state}\nclick: {click.click_state}\n== special: {click.special} =="
        label.config(text=text + text_state)

        profile = (
            f"[{now}]\n"
            f"=== {data[selection]['label']} ===\n"
            f"    misc_state: {click.misc_state}\n"
            f"    elven_state: {click.elven_state}\n"
            f"    click_state: {click.click_state}\n"
            "\n"
            f"    misc_time_random: {click.misc_time_random}\n"
            f"    misc_time_constant: {click.misc_time_constant}\n"
            "\n"
            f"    elven_time_random: {click.elven_time_random}\n"
            f"    elven_time_constant: {click.elven_time_constant}\n"
            "\n"
            f"    click_time_random: {click.click_time_random}\n"
            f"    click_time_constant: {click.click_time_constant}\n"
            "\n"
            f"    special: {click.special}\n"
        )
        print(profile)


if __name__ == "__main__":
    root = initialize_ui()

    click = Click()
    click.start()

    with open("data.json") as file:
        data = json.load(file)

    var = IntVar(value=len(data))

    for index, element in enumerate(data):
        radio_button = Radiobutton(
            root,
            text=data[element]["label"],
            variable=var,
            value=index + 1,
            command=set_values,
        )
        radio_button.pack(anchor=W)

    label = Label(root)
    label.pack()
    root.update()

    while True:
        sleep(0.1)
        root.update()
