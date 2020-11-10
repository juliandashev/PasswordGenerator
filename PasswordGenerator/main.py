# Import the libraries im gonna need to create the app
import tkinter as tk
import random
import string
from tkinter import *
from tkinter import filedialog, messagebox
from tkinter import font


# This functions creates the Widgets for the GUI
def Widgets():
    # ----------------- Labels to gute the user what to do! -----------------------------
    # Password label its position in the GUI and making it readonly so the user can only copy not change the password
    password_label = \
        Label(win, text="Your password:", bg=bg_color, fg="white", font=global_font)

    password_label.grid(row=1, column=0, padx=10, pady=10)

    # Username label its position in the GUI
    username_label = \
        Label(win, text="Your username:", bg=bg_color, fg="white", font=global_font)

    username_label.grid(row=2, column=0, padx=10, pady=10)

    # App name label its position in the GUI
    app_name_label = \
        Label(win, text="Enter app:", bg=bg_color, fg="white", font=global_font)

    app_name_label.grid(row=3, column=0, padx=10, pady=10)

    # ----------------- Creating textboxes where the data is shown ------------------------
    # Password textbox and its position in the GUI
    win.passowrd_textbox = \
        Entry(win, width=50, textvariable=passowrd, state="readonly", readonlybackground=fg_color, fg="black", font=textBox_font)

    win.passowrd_textbox.grid(row=1, column=1, pady=5, padx=5)

    # Username textbox and its position in the GUI
    win.username_textbox = \
        Entry(win, width=50, textvariable=username, bg=fg_color, fg="black", font=textBox_font)

    win.username_textbox.grid(row=2, column=1, pady=5, padx=5)

    # App name textbox and its position in the GUI
    win.app_name_textbox = \
        Entry(win, width=50, textvariable=app_name, bg=fg_color, fg="black", font=textBox_font)

    win.app_name_textbox.grid(row=3, column=1, pady=5, padx=5)

    #  ---------------- Creating buttons to generate the password, save it and clear the search --------------
    # Creating a button to generate the password
    generate_button = \
        Button(win, text="Generate", command=GeneratePassowrd, width=10, bg=fg_color, fg="white", font=global_font)

    generate_button.grid(row=1, column=2, pady=5, padx=5)

    # Creating a button to Clear the information dispayed
    clear_button = \
        Button(win, text="Clear", command=ClearEverything, width=10, bg=fg_color, fg="white", font=global_font)

    clear_button.grid(row=3, column=2, pady=5, padx=5)

    # Creating a button to Save the password and the username in a textfile created by the user
    save_button = \
        Button(win, text="Save", command=SavePassword, width=10, bg=fg_color, fg="white", font=global_font)

    save_button.grid(row=2, column=2, pady=5, padx=5)


# This function generates the password
def GeneratePassowrd():
    # emptying the string to prevent from stacking different symbols
    passowrd.set("")

    letters = string.ascii_letters
    numbers = string.digits
    symbols = "!@#$%^&*-_?"

    # Combining every letter (even the Capital once) with every number and sybols to make the password stronger
    everything = f"{letters}{numbers}{symbols}"

    everything = list(everything)
    random.shuffle(everything)

    # creating the password and giving it a length
    new_password = random.choices(everything, k=password_lenght.get())
    passowrd.set(''.join(new_password))


# This function saves the password
def SavePassword():
    # Here the program asks for an existing text file to store the data
    download_dir = filedialog.askopenfilename()
    file_path.set(download_dir)

    # if there isn't such file, It displays a message to the user to select it
    try:
        fw = open(f"{file_path.get()}", "a")
    except FileNotFoundError:
        messagebox.showinfo("Error", "Please, select a text file to save your data!")
        return

    # Checking if the user actually entered a username or app name.. otherwise the document wont contain anything, but the password
    if len(username.get()) == 0 or len(app_name.get()) == 0:
        messagebox.showinfo("Error", "Please enter your username or app name!")
        return

    # Writing the information on the text document
    fw.write(f"[{app_name.get()}] account: [{username.get()}] - [{passowrd.get()}]\n")
    fw.close()

    # A final message to tell us that everything is alright and everything is saved
    messagebox.showinfo("Comeplete", f"You password have been saved at {file_path.get()}")


# Clearing everything
def ClearEverything():
    passowrd.set("")
    username.set("")
    app_name.set("")


# Creating the Instance
win = tk.Tk()

# Making it resizable and adding a title to the program
win.resizable(False, False)
win.title("Password Generator")

# Saving the colors im using
bg_color = "#2d2c2c"
fg_color = "#de3a29"

# Saving the fonts im using for the labes and textboxes
textBox_font = font.Font(family='Courier New', size=14, slant="italic")
global_font = font.Font(family='Courier New', size=12, weight="bold", slant="italic")

# Scoping variables so i can use the anywhere
app_name = StringVar(master=win)
passowrd = StringVar(master=win)
username = StringVar(master=win)
password_lenght = IntVar(master=win)
file_path = StringVar(master=win)

# Setting a random password lenght
rand_num = random.randrange(13, 20)
password_lenght.set(rand_num)

# Adding a color the the GUI
win.configure(bg=bg_color)

# Calling the Widgets() function to dispaly everything
Widgets()

# Start the GUI/ Create the main loop
win.mainloop()
