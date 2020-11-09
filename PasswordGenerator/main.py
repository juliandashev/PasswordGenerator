import tkinter as tk
import random
import string
from tkinter import *
from tkinter import filedialog, messagebox
from tkinter import font


def Widgets():
    password_label = \
        Label(win, text="Your password:", bg=bg_color, fg="white", font=global_font)

    password_label.grid(row=1, column=0, padx=10, pady=10)

    win.passowrd_textbox = \
        Entry(win, width=50, textvariable=passowrd, bg=fg_color, fg="black", font=textBox_font)

    win.passowrd_textbox.grid(row=1, column=1, pady=5, padx=5)

    generate_button = \
        Button(win, text="Generate", command=GeneratePassowrd, width=10, bg=fg_color, fg="white", font=global_font)

    generate_button.grid(row=1, column=2, pady=5, padx=5)

    clear_button = \
        Button(win, text="Clear", command=ClearPassword, width=10, bg=fg_color, fg="white", font=global_font)

    clear_button.grid(row=4, column=2, pady=5, padx=5)

    save_button = \
        Button(win, text="Save", command=SavePassword, width=10, bg=fg_color, fg="white", font=global_font)

    save_button.grid(row=3, column=2, pady=5, padx=5)


def GeneratePassowrd():
    passowrd.set("")

    letters = string.ascii_letters
    numbers = string.digits
    symbols = "!@#$%^&*-_?"

    everything = f"{letters}{numbers}{symbols}"

    everything = list(everything)
    random.shuffle(everything)

    new_password = random.choices(everything, k=password_lenght.get())
    passowrd.set(''.join(new_password))


def SavePassword():
    download_dir = filedialog.askdirectory(title="Choose a folder")

    file_path.set(download_dir)

    try:
        fw = open(f"{file_path.get()}\passwords.txt", "x")
    except FileExistsError:
        fw = open(f"{file_path.get()}\passwords.txt", "a")

    fw.write(f"{passowrd.get()} - with length:{password_lenght.get()}\n")
    fw.close()


def ClearPassword():
    passowrd.set("")


win = tk.Tk()
win.resizable(False, False)
win.title("Password Generator")

bg_color = "#2d2c2c"
fg_color = "#de3a29"

textBox_font = font.Font(family='Courier New', size=14, slant="italic")
global_font = font.Font(family='Courier New', size=12, weight="bold", slant="italic")

passowrd = StringVar(master=win)
username = StringVar(master=win)
password_lenght = IntVar(master=win)
file_path = StringVar(master=win)

password_lenght.set(10)

win.configure(bg=bg_color)

Widgets()

win.mainloop()
