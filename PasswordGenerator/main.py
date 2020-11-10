import tkinter as tk
import random
import string
from tkinter import *
from tkinter import filedialog, messagebox
from tkinter import font


def Widgets():
    # ----------------- Labels to gute the user what to do! -----------------------------
    password_label = \
        Label(win, text="Your password:", bg=bg_color, fg="white", font=global_font)

    password_label.grid(row=1, column=0, padx=10, pady=10)

    username_label = \
        Label(win, text="Your username:", bg=bg_color, fg="white", font=global_font)

    username_label.grid(row=2, column=0, padx=10, pady=10)

    app_name_label = \
        Label(win, text="Enter app:", bg=bg_color, fg="white", font=global_font)

    app_name_label.grid(row=3, column=0, padx=10, pady=10)

    # ----------------- Creating textboxes where the data is shown ------------------------
    win.passowrd_textbox = \
        Entry(win, width=50, textvariable=passowrd, state="readonly", readonlybackground=fg_color, fg="black", font=textBox_font)

    win.passowrd_textbox.grid(row=1, column=1, pady=5, padx=5)

    win.username_textbox = \
        Entry(win, width=50, textvariable=username, bg=fg_color, fg="black", font=textBox_font)

    win.username_textbox.grid(row=2, column=1, pady=5, padx=5)

    win.app_name_textbox = \
        Entry(win, width=50, textvariable=app_name, bg=fg_color, fg="black", font=textBox_font)

    win.app_name_textbox.grid(row=3, column=1, pady=5, padx=5)

    #  ---------------- Creating buttons to generate the password, save it and clear the search --
    generate_button = \
        Button(win, text="Generate", command=GeneratePassowrd, width=10, bg=fg_color, fg="white", font=global_font)

    generate_button.grid(row=1, column=2, pady=5, padx=5)

    clear_button = \
        Button(win, text="Clear", command=ClearEverything, width=10, bg=fg_color, fg="white", font=global_font)

    clear_button.grid(row=3, column=2, pady=5, padx=5)

    save_button = \
        Button(win, text="Save", command=SavePassword, width=10, bg=fg_color, fg="white", font=global_font)

    save_button.grid(row=2, column=2, pady=5, padx=5)


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
    download_dir = filedialog.askopenfilename()
    file_path.set(download_dir)

    try:
        fw = open(f"{file_path.get()}", "a")
    except FileNotFoundError:
        messagebox.showinfo("Error", "Please, select a text file to save your data!")
        return

    fw.write(f"[{app_name.get()}] account: [{username.get()}] - [{passowrd.get()}]\n")
    fw.close()

    messagebox.showinfo("Comeplete", f"You password have been saved at {file_path.get()}")


def ClearEverything():
    passowrd.set("")
    username.set("")
    app_name.set("")


win = tk.Tk()
win.resizable(False, False)
win.title("Password Generator")

bg_color = "#2d2c2c"
fg_color = "#de3a29"

textBox_font = font.Font(family='Courier New', size=14, slant="italic")
global_font = font.Font(family='Courier New', size=12, weight="bold", slant="italic")

app_name = StringVar(master=win)
passowrd = StringVar(master=win)
username = StringVar(master=win)
password_lenght = IntVar(master=win)
file_path = StringVar(master=win)

rand_num = random.randrange(10, 20)
password_lenght.set(rand_num)

win.configure(bg=bg_color)

Widgets()

win.mainloop()
