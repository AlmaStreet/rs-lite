from clicker import Click
from datetime import datetime
from tkinter import IntVar, Label, Radiobutton, Tk, W
from data import profile_data


def initialize_ui():
    tk = Tk()
    tk.title("AFK Selection")
    tk.geometry("240x720")
    return tk


def set_values():
    selection = str(var.get())
    if selection in profile_data:
        click.update_data(profile_data[selection])
        print_profile(selection)
    update_label(selection)


def update_label(selection):
    text = f"You selected the option {selection}"
    text_state = f"\nmisc: {click.misc_state}\nelven: {click.elven_state}\nclick: {click.click_state}\n== special: {click.special} =="
    label.config(text=text + text_state)


def print_profile(selection):
    now = datetime.now().strftime("%H:%M:%S")
    profile_info = profile_data[selection]
    profile = f"[{now}]\n=== {profile_info['label']} ===\n"
    for key in [
        "misc_state",
        "elven_state",
        "click_state",
        "misc_time_random",
        "misc_time_constant",
        "elven_time_random",
        "elven_time_constant",
        "click_time_random",
        "click_time_constant",
        "special",
    ]:
        profile += f"    {key}: {profile_info[key]}\n"
    print(profile)


def malloc_setup():
    import tracemalloc

    tracemalloc.start()
    return tracemalloc


def print_malloc_stats(t_malloc):
    snapshot = t_malloc.take_snapshot()
    top_stats = snapshot.statistics("lineno")
    for stat in top_stats[:10]:
        print(stat)


if __name__ == "__main__":
    debug = False

    root = initialize_ui()
    click = Click()
    click.start()

    var = IntVar(value=1)

    for index, element in enumerate(profile_data):
        Radiobutton(
            root,
            text=profile_data[element]["label"],
            variable=var,
            value=index + 1,
            command=set_values,
        ).pack(anchor=W)

    label = Label(root)
    label.pack()

    if debug:
        t_malloc = malloc_setup()

    root.mainloop()

    if debug:
        print_malloc_stats(t_malloc)
