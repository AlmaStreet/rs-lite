#
# d = {
#         1: {
#             "label": "Fishing",
#         "misc_state": True,
#         "elven_state": True,
#         "click_state": True,
#         "misc_time_random": 20,
#         "misc_time_constant": 30,
#         "elven_time_random": 35,
#         "elven_time_constant": 60,
#         "click_time_random": 18,
#         "click_time_constant": 25,
#     },
#         2: {
#             "label": "Click only",
#         "misc_state": False,
#         "elven_state": False,
#         "click_state": True,
#         "misc_time_random": 20,
#         "misc_time_constant": 30,
#         "elven_time_random": 20,
#         "elven_time_constant": 30,
#         "click_time_random": 28,
#         "click_time_constant": 11,
#     },
#         3: {
#             "label": "Glacor",
#         "misc_state": False,
#         "elven_state": True,
#         "click_state": True,
#         "misc_time_random": 30,
#         "misc_time_constant": 80,
#         "elven_time_random": 50,
#         "elven_time_constant": 130,
#         "click_time_random": 23,
#         "click_time_constant": 30,
#     },
#         4: {
#             "label": "PSD AFK",
#         "misc_state": True,
#         "elven_state": False,
#         "click_state": True,
#         "misc_time_random": 28,
#         "misc_time_constant": 343,
#         "elven_time_random": 30,
#         "elven_time_constant": 30,
#         "click_time_random": 35,
#         "click_time_constant": 38,
#     },
#         5: {
#             "label": "Rathis/Corp AFK",
#         "misc_state": True,
#         "elven_state": True,
#         "click_state": True,
#         "misc_time_random": 10,
#         "misc_time_constant": 347,
#         "elven_time_random": 30,
#         "elven_time_constant": 25,
#         "click_time_random": 21,
#         "click_time_constant": 23,
#     },
#         6: {
#             "label": "Orikalka AFK",
#         "misc_state": True,
#         "elven_state": True,
#         "click_state": True,
#         "misc_time_random": 8,
#         "misc_time_constant": 357,
#         "elven_time_random": 20,
#         "elven_time_constant": 690,
#         "click_time_random": 23,
#         "click_time_constant": 30,
#     },
#         7: {
#             "label": "KBD AFK",
#         "misc_state": True,
#         "elven_state": True,
#         "click_state": True,
#         "misc_time_random": 18,
#         "misc_time_constant": 700,
#         "elven_time_random": 30,
#         "elven_time_constant": 25,
#         "click_time_random": 23,
#         "click_time_constant": 30,
#     },
#         8: {
#             "label": "Mining with porters",
#         "misc_state": True,
#         "elven_state": True,
#         "click_state": True,
#         "misc_time_random": 60,
#         "misc_time_constant": 90,
#         "elven_time_random": 30,
#         "elven_time_constant": 25,
#         "click_time_random": 28,
#         "click_time_constant": 28,
#     },
#         9: {
#             "label": "Kalgs AFK",
#         "misc_state": True,
#         "elven_state": True,
#         "click_state": True,
#         "misc_time_random": 30,
#         "misc_time_constant": 80,
#         "elven_time_random": 30,
#         "elven_time_constant": 25,
#         "click_time_random": 20,
#         "click_time_constant": 690,
#     },
#         10: {
#             "label": "Zuk AFK",
#         "misc_state": True,
#         "elven_state": True,
#         "click_state": True,
#         "misc_time_random": 30,
#         "misc_time_constant": 25,
#         "elven_time_random": 20,
#         "elven_time_constant": 690,
#         "click_time_random": 12,
#         "click_time_constant": 12,
#     },
#         11: {
#             "label": "Glacor Oldak AFK",
#         "misc_state": True,
#         "elven_state": True,
#         "click_state": True,
#         "misc_time_random": 15,
#         "misc_time_constant": 60,
#         "elven_time_random": 20,
#         "elven_time_constant": 250,
#         "click_time_random": 60,
#         "click_time_constant": 600,
#     },
#         12: {
#             "label": "Rune Dragon AFK",
#         "misc_state": True,
#         "elven_state": True,
#         "click_state": True,
#         "misc_time_random": 8,
#         "misc_time_constant": 357,
#         "elven_time_random": 8,
#         "elven_time_constant": 348,
#         "click_time_random": 23,
#         "click_time_constant": 30,
#     },
#         13: {
#             "label": "Adamant Dragon AFK",
#         "misc_state": True,
#         "elven_state": True,
#         "click_state": True,
#         "misc_time_random": 20,
#         "misc_time_constant": 690,
#         "elven_time_random": 20,
#         "elven_time_constant": 690,
#         "click_time_random": 23,
#         "click_time_constant": 30,
#     },
#         14: {
#             "label": "Off",
#         "misc_state": False,
#         "elven_state": False,
#         "click_state": False,
#         "misc_time_random": 30,
#         "misc_time_constant": 30,
#         "elven_time_random": 30,
#         "elven_time_constant": 30,
#         "click_time_random": 20,
#         "click_time_constant": 20,
#     },
# }
#
# root = Tk()
# root.title("AFK Selection")
# root.geometry("200x420")
# var = IntVar(value=len(d))
#
# index = 1
# for element in d:
#     radio_button = Radiobutton(
#         root, text=element, variable=var, value=element, command=set_values
#     )
#     radio_button.pack(anchor=W)
#
# R1 = Radiobutton(root, text="Fishing", variable=var, value=1, command=set_values)
# R1.pack(anchor=W)
#
#
#
# selection = var.get()
#     # selection = 1
#
# # fishing
#     if selection == 1:
#         print("[", now, "] === Fishing ===")
#         click.misc_state = True
#         click.elven_state = True
#         click.click_state = True
#
#         click.misc_time_random = 20
#         click.misc_time_constant = 30
#
#         click.elven_time_random = 35
#         click.elven_time_constant = 60
#
#         click.click_time_random = 18
#         click.click_time_constant = 25
#
#         text_state = f"\nmisc: {click.misc_state}\nelven: {click.elven_state}\nclick: {click.click_state}"
#         label.config(text=text + text_state)
#
#
#
# def set_values():
#     selection = var.get()
#     # selection = 1
#
#     text = "You selected the option" + str(selection)
#
#     now = datetime.now().strftime("%H:%M:%S")
#
#     # fishing
#     if selection in d:
#         print("[", now, f"] === {selection} ===")
#         click.misc_state = d[selection]['misc_state']
#         click.elven_state = d[selection]['elven_state']
#         click.click_state = d[selection]['click_state']
#
#         click.misc_time_random = d[selection]['misc_time_random']
#         click.misc_time_constant = d[selection]['misc_time_constant']
#
#         click.elven_time_random = d[selection]['elven_time_random']
#         click.elven_time_constant = d[selection]['elven_time_constant']
#
#         click.click_time_random = d[selection]['click_time_random']
#         click.click_time_constant = d[selection]['click_time_constant']
#
#         text_state = f"\nmisc: {click.misc_state}\nelven: {click.elven_state}\nclick: {click.click_state}"
#         label.config(text=text + text_state)
#
#
# from clicker import Click
# from datetime import datetime
# from time import time, sleep
# from tkinter import IntVar, Label, Radiobutton, Tk, W
#
# click = Click()
# click.start()
#
# d = {
#     1: {
#         "label": "Fishing",
#         "misc_state": True,
#         "elven_state": True,
#         "click_state": True,
#         "misc_time_random": 20,
#         "misc_time_constant": 30,
#         "elven_time_random": 35,
#         "elven_time_constant": 60,
#         "click_time_random": 18,
#         "click_time_constant": 25,
#     },
#     2: {
#         "label": "Click only",
#         "misc_state": False,
#         "elven_state": False,
#         "click_state": True,
#         "misc_time_random": 20,
#         "misc_time_constant": 30,
#         "elven_time_random": 20,
#         "elven_time_constant": 30,
#         "click_time_random": 28,
#         "click_time_constant": 11,
#     },
#     3: {
#         "label": "Glacor",
#         "misc_state": False,
#         "elven_state": True,
#         "click_state": True,
#         "misc_time_random": 30,
#         "misc_time_constant": 80,
#         "elven_time_random": 50,
#         "elven_time_constant": 130,
#         "click_time_random": 23,
#         "click_time_constant": 30,
#     },
#     4: {
#         "label": "PSD AFK",
#         "misc_state": True,
#         "elven_state": False,
#         "click_state": True,
#         "misc_time_random": 28,
#         "misc_time_constant": 343,
#         "elven_time_random": 30,
#         "elven_time_constant": 30,
#         "click_time_random": 35,
#         "click_time_constant": 38,
#     },
#     5: {
#         "label": "Rathis/Corp AFK",
#         "misc_state": True,
#         "elven_state": True,
#         "click_state": True,
#         "misc_time_random": 10,
#         "misc_time_constant": 347,
#         "elven_time_random": 30,
#         "elven_time_constant": 25,
#         "click_time_random": 21,
#         "click_time_constant": 23,
#     },
#     6: {
#         "label": "Orikalka AFK",
#         "misc_state": True,
#         "elven_state": True,
#         "click_state": True,
#         "misc_time_random": 8,
#         "misc_time_constant": 357,
#         "elven_time_random": 20,
#         "elven_time_constant": 690,
#         "click_time_random": 23,
#         "click_time_constant": 30,
#     },
#     7: {
#         "label": "KBD AFK",
#         "misc_state": True,
#         "elven_state": True,
#         "click_state": True,
#         "misc_time_random": 18,
#         "misc_time_constant": 700,
#         "elven_time_random": 30,
#         "elven_time_constant": 25,
#         "click_time_random": 23,
#         "click_time_constant": 30,
#     },
#     8: {
#         "label": "Mining with porters",
#         "misc_state": True,
#         "elven_state": True,
#         "click_state": True,
#         "misc_time_random": 60,
#         "misc_time_constant": 90,
#         "elven_time_random": 30,
#         "elven_time_constant": 25,
#         "click_time_random": 28,
#         "click_time_constant": 28,
#     },
#     9: {
#         "label": "Kalgs AFK",
#         "misc_state": True,
#         "elven_state": True,
#         "click_state": True,
#         "misc_time_random": 30,
#         "misc_time_constant": 80,
#         "elven_time_random": 30,
#         "elven_time_constant": 25,
#         "click_time_random": 20,
#         "click_time_constant": 690,
#     },
#     10: {
#         "label": "Zuk AFK",
#         "misc_state": True,
#         "elven_state": True,
#         "click_state": True,
#         "misc_time_random": 30,
#         "misc_time_constant": 25,
#         "elven_time_random": 20,
#         "elven_time_constant": 690,
#         "click_time_random": 12,
#         "click_time_constant": 12,
#     },
#     11: {
#         "label": "Glacor Oldak AFK",
#         "misc_state": True,
#         "elven_state": True,
#         "click_state": True,
#         "misc_time_random": 15,
#         "misc_time_constant": 60,
#         "elven_time_random": 20,
#         "elven_time_constant": 250,
#         "click_time_random": 60,
#         "click_time_constant": 600,
#     },
#     12: {
#         "label": "Rune Dragon AFK",
#         "misc_state": True,
#         "elven_state": True,
#         "click_state": True,
#         "misc_time_random": 8,
#         "misc_time_constant": 357,
#         "elven_time_random": 8,
#         "elven_time_constant": 348,
#         "click_time_random": 23,
#         "click_time_constant": 30,
#     },
#     13: {
#         "label": "Adamant Dragon AFK",
#         "misc_state": True,
#         "elven_state": True,
#         "click_state": True,
#         "misc_time_random": 20,
#         "misc_time_constant": 690,
#         "elven_time_random": 20,
#         "elven_time_constant": 690,
#         "click_time_random": 23,
#         "click_time_constant": 30,
#     },
#     14: {
#         "label": "Off",
#         "misc_state": False,
#         "elven_state": False,
#         "click_state": False,
#         "misc_time_random": 30,
#         "misc_time_constant": 30,
#         "elven_time_random": 30,
#         "elven_time_constant": 30,
#         "click_time_random": 20,
#         "click_time_constant": 20,
#     },
# }
#
#
# def set_values():
#     selection = var.get()
#
#     text = "You selected the option" + str(selection)
#     now = datetime.now().strftime("%H:%M:%S")
#
#     if selection in d:
#         print("[", now, f"] === {d[selection]['label']} ===")
#         click.misc_state = d[selection]["misc_state"]
#         click.elven_state = d[selection]["elven_state"]
#         click.click_state = d[selection]["click_state"]
#
#         click.misc_time_random = d[selection]["misc_time_random"]
#         click.misc_time_constant = d[selection]["misc_time_constant"]
#
#         click.elven_time_random = d[selection]["elven_time_random"]
#         click.elven_time_constant = d[selection]["elven_time_constant"]
#
#         click.click_time_random = d[selection]["click_time_random"]
#         click.click_time_constant = d[selection]["click_time_constant"]
#
#         print(f"misc_state: {click.misc_state}")
#         print(f"elven_state: {click.elven_state}")
#         print(f"click_state: {click.click_state}")
#         print()
#         print(f"misc_time_random: {click.misc_time_random}")
#         print(f"misc_time_constant: {click.misc_time_constant}")
#         print()
#         print(f"elven_time_random: {click.elven_time_random}")
#         print(f"elven_time_constant: {click.elven_time_constant}")
#         print()
#         print(f"click_time_random: {click.click_time_random}")
#         print(f"click_time_constant: {click.click_time_constant}")
#
#         text_state = f"\nmisc: {click.misc_state}\nelven: {click.elven_state}\nclick: {click.click_state}"
#         label.config(text=text + text_state)
#
#
# # def set_values():
# #     selection = var.get()
# #     # selection = 1
#
# #     text = "You selected the option" + str(selection)
#
# #     now = datetime.now().strftime("%H:%M:%S")
#
# #     # fishing
# #     if selection == 1:
# #         print("[", now, "] === Fishing ===")
# #         click.misc_state = True
# #         click.elven_state = True
# #         click.click_state = True
#
# #         click.misc_time_random = 20
# #         click.misc_time_constant = 30
#
# #         click.elven_time_random = 35
# #         click.elven_time_constant = 60
#
# #         click.click_time_random = 18
# #         click.click_time_constant = 25
#
# #         text_state = f"\nmisc: {click.misc_state}\nelven: {click.elven_state}\nclick: {click.click_state}"
# #         label.config(text=text + text_state)
#
# #     # click only
# #     elif selection == 2:
# #         print("[", now, "] === Click only ===")
# #         click.misc_state = False
# #         click.elven_state = False
# #         click.click_state = True
#
# #         click.misc_time_random = 20
# #         click.misc_time_constant = 30
#
# #         click.elven_time_random = 20
# #         click.elven_time_constant = 30
#
# #         click.click_time_random = 28
# #         click.click_time_constant = 11
#
# #         text_state = f"\nmisc: {click.misc_state}\nelven: {click.elven_state}\nclick: {click.click_state}"
# #         label.config(text=text + text_state)
#
# #     # glacor
# #     elif selection == 3:
# #         print("[", now, "] === Glacor ===")
# #         click.misc_state = False
# #         click.elven_state = True
# #         click.click_state = True
#
# #         click.misc_time_random = 30
# #         click.misc_time_constant = 80
#
# #         click.elven_time_random = 50
# #         click.elven_time_constant = 130
#
# #         click.click_time_random = 23
# #         click.click_time_constant = 30
#
# #         text_state = f"\nmisc: {click.misc_state}\nelven: {click.elven_state}\nclick: {click.click_state}"
# #         label.config(text=text + text_state)
#
# #     # PSD AFK
# #     elif selection == 4:
# #         print("[", now, "] === PSD AFK ===")
# #         click.misc_state = True
# #         click.elven_state = False
# #         click.click_state = True
#
# #         click.misc_time_random = 28
# #         click.misc_time_constant = 343
#
# #         click.elven_time_random = 30
# #         click.elven_time_constant = 30
#
# #         click.click_time_random = 35
# #         click.click_time_constant = 38
#
# #         text_state = f"\nmisc: {click.misc_state}\nelven: {click.elven_state}\nclick: {click.click_state}"
# #         label.config(text=text + text_state)
#
# #     # Rathis/corp (elven + overload)
# #     elif selection == 5:
# #         print("[", now, "] === Rathis/Corp AFK ===")
# #         click.misc_state = True
# #         click.elven_state = True
# #         click.click_state = True
#
# #         # overload
# #         click.misc_time_random = 10
# #         click.misc_time_constant = 347
#
# #         click.elven_time_random = 30
# #         click.elven_time_constant = 25
# #         # loot
# #         click.click_time_random = 21
# #         click.click_time_constant = 23
#
# #         text_state = f"\nmisc: {click.misc_state}\nelven: {click.elven_state}\nclick: {click.click_state}"
# #         label.config(text=text + text_state)
#
# #     # Orikalka (Animate + overload)
# #     elif selection == 6:
# #         print("[", now, "] === Orikalka AFK ===")
# #         click.misc_state = True
# #         click.elven_state = True
# #         click.click_state = True
#
# #         # overload
# #         click.misc_time_random = 8
# #         click.misc_time_constant = 357
# #         # animate dead
# #         click.elven_time_random = 20
# #         click.elven_time_constant = 690
# #         # loot
# #         click.click_time_random = 23
# #         click.click_time_constant = 30
#
# #         text_state = f"\nmisc: {click.misc_state}\nelven: {click.elven_state}\nclick: {click.click_state}"
# #         label.config(text=text + text_state)
#
# #     # KBD (dom marker + extended antifire)
# #     elif selection == 7:
# #         print("[", now, "] === KBD AFK ===")
# #         click.misc_state = True
# #         click.elven_state = True
# #         click.click_state = True
#
# #         # extended antifire
# #         click.misc_time_random = 18
# #         click.misc_time_constant = 700
# #         # dom marker
# #         click.elven_time_random = 30
# #         click.elven_time_constant = 25
# #         # loot
# #         click.click_time_random = 23
# #         click.click_time_constant = 30
#
# #         text_state = f"\nmisc: {click.misc_state}\nelven: {click.elven_state}\nclick: {click.click_state}"
# #         label.config(text=text + text_state)
#
# #     # Mining (elven + porter)
# #     elif selection == 8:
# #         print("[", now, "] === Mining with porters ===")
# #         click.misc_state = True
# #         click.elven_state = True
# #         click.click_state = True
#
# #         # click porter
# #         click.misc_time_random = 60
# #         click.misc_time_constant = 90
# #         # dom marker
# #         click.elven_time_random = 30
# #         click.elven_time_constant = 25
# #         # loot
# #         click.click_time_random = 28
# #         click.click_time_constant = 28
#
# #         text_state = f"\nmisc: {click.misc_state}\nelven: {click.elven_state}\nclick: {click.click_state}"
# #         label.config(text=text + text_state)
#
# #     # Kalgs (elven + venca + animate dead click)
# #     elif selection == 9:
# #         print("[", now, "] === Kalgs AFK ===")
# #         click.misc_state = True
# #         click.elven_state = True
# #         click.click_state = True
#
# #         # overload
# #         click.misc_time_random = 30
# #         click.misc_time_constant = 80
#
# #         click.elven_time_random = 30
# #         click.elven_time_constant = 25
# #         # loot
# #         click.click_time_random = 20
# #         click.click_time_constant = 690
#
# #         text_state = f"\nmisc: {click.misc_state}\nelven: {click.elven_state}\nclick: {click.click_state}"
# #         label.config(text=text + text_state)
#
# #     # Zuk AFK (Animate + elven + action)
# #     elif selection == 10:
# #         print("[", now, "] === Zuk AFK ===")
# #         click.misc_state = True
# #         click.elven_state = True
# #         click.click_state = True
#
# #         # elven
# #         click.misc_time_random = 30
# #         click.misc_time_constant = 25
# #         # animate dead
# #         click.elven_time_random = 20
# #         click.elven_time_constant = 690
# #         # action button
# #         click.click_time_random = 12
# #         click.click_time_constant = 12
#
# #         text_state = f"\nmisc: {click.misc_state}\nelven: {click.elven_state}\nclick: {click.click_state}"
# #         label.config(text=text + text_state)
#
# #     # Glacor Oldak AFK (cannon + dom marker + action)
# #     elif selection == 11:
# #         print("[", now, "] === Glacor Oldak AFK ===")
# #         click.misc_state = True
# #         click.elven_state = True
# #         click.click_state = True
#
# #         # action button
# #         click.misc_time_random = 15
# #         click.misc_time_constant = 60
# #         # dom marker
# #         click.elven_time_random = 20
# #         click.elven_time_constant = 250
# #         # click oldak coil
# #         click.click_time_random = 60
# #         click.click_time_constant = 600
#
# #         text_state = f"\nmisc: {click.misc_state}\nelven: {click.elven_state}\nclick: {click.click_state}"
# #         label.config(text=text + text_state)
#
# #     # Rune Dragon (aggro pot + overload)
# #     elif selection == 12:
# #         print("[", now, "] === Rune Dragon AFK ===")
# #         click.misc_state = True
# #         click.elven_state = True
# #         click.click_state = True
#
# #         # aggro pot
# #         click.misc_time_random = 8
# #         click.misc_time_constant = 357
# #         # overload
# #         click.elven_time_random = 8
# #         click.elven_time_constant = 348
# #         # loot
# #         click.click_time_random = 23
# #         click.click_time_constant = 30
#
# #         text_state = f"\nmisc: {click.misc_state}\nelven: {click.elven_state}\nclick: {click.click_state}"
# #         label.config(text=text + text_state)
#
# #     # Adamant Dragon (Animate + super anti)
# #     elif selection == 13:
# #         print("[", now, "] === Adamant Dragon AFK ===")
# #         click.misc_state = True
# #         click.elven_state = True
# #         click.click_state = True
#
# #         # overload
# #         click.misc_time_random = 20
# #         click.misc_time_constant = 690
# #         # animate dead
# #         click.elven_time_random = 20
# #         click.elven_time_constant = 690
# #         # loot
# #         click.click_time_random = 23
# #         click.click_time_constant = 30
#
# #         text_state = f"\nmisc: {click.misc_state}\nelven: {click.elven_state}\nclick: {click.click_state}"
# #         label.config(text=text + text_state)
#
# #     # off
# #     else:
# #         print("[", now, "] === Off ===")
# #         click.misc_state = False
# #         click.elven_state = False
# #         click.click_state = False
#
# #         click.misc_time_random = 30
# #         click.misc_time_constant = 30
#
# #         click.elven_time_random = 30
# #         click.elven_time_constant = 30
#
# #         click.click_time_random = 20
# #         click.click_time_constant = 20
#
# #         # resets previous random times
# #         click.misc_time = time()
# #         click.elven_time = time()
# #         click.click_time = time()
#
# #         text_state = f"\nmisc: {click.misc_state}\nelven: {click.elven_state}\nclick: {click.click_state}"
# #         label.config(text=text + text_state)
#
#
# root = Tk()
# root.title("AFK Selection")
# root.geometry("200x420")
#
# var = IntVar(value=len(d))
#
# index = 1
# for element in d:
#     radio_button = Radiobutton(
#         root, text=d[element]["label"], variable=var, value=index, command=set_values
#     )
#     index += 1
#     radio_button.pack(anchor=W)
#
#
# # var = IntVar(value=20)
# # R1 = Radiobutton(root, text="Fishing", variable=var, value=1, command=set_values)
# # R1.pack(anchor=W)
#
# # R2 = Radiobutton(root, text="Click only", variable=var, value=2, command=set_values)
# # R2.pack(anchor=W)
#
# # R3 = Radiobutton(root, text="Glacor", variable=var, value=3, command=set_values)
# # R3.pack(anchor=W)
#
# # R4 = Radiobutton(root, text="PSD AFK", variable=var, value=4, command=set_values)
# # R4.pack(anchor=W)
#
# # R5 = Radiobutton(
# #     root, text="Rathis/Corp AFK", variable=var, value=5, command=set_values
# # )
# # R5.pack(anchor=W)
#
# # R5 = Radiobutton(root, text="Orikalka AFK", variable=var, value=6, command=set_values)
# # R5.pack(anchor=W)
#
# # R5 = Radiobutton(root, text="KBD AFK", variable=var, value=7, command=set_values)
# # R5.pack(anchor=W)
#
# # R5 = Radiobutton(
# #     root, text="Mining with porters", variable=var, value=8, command=set_values
# # )
# # R5.pack(anchor=W)
#
# # R5 = Radiobutton(root, text="Kalgs AFK", variable=var, value=9, command=set_values)
# # R5.pack(anchor=W)
#
# # R5 = Radiobutton(root, text="Zuk AFK", variable=var, value=10, command=set_values)
# # R5.pack(anchor=W)
#
# # R5 = Radiobutton(
# #     root, text="Glacor Oldak AFK", variable=var, value=11, command=set_values
# # )
# # R5.pack(anchor=W)
#
# # R5 = Radiobutton(
# #     root, text="Rune Dragon AFK", variable=var, value=12, command=set_values
# # )
# # R5.pack(anchor=W)
#
# # R5 = Radiobutton(
# #     root, text="Adamant Dragon AFK", variable=var, value=13, command=set_values
# # )
# # R5.pack(anchor=W)
#
# # R6 = Radiobutton(root, text="Off", variable=var, value=20, command=set_values)
# # R6.pack(anchor=W)
#
# label = Label(root)
# label.pack()
# root.update()
#
# while True:
#     sleep(0.1)
#     root.update()
#
#     # print(f"click.state: {click.state}")
#     # print("fps: {}".format(1 / (time() - last_time)))
#
#     # Press "q" to quit
#     if 0xFF == ord("q"):
#         click.stop()
#         break



# TODO
# add cannonball maker
# add armor spikes maker
# add veno dino afk