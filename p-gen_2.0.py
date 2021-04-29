from tkinter import *
from tkinter.ttk import *
import subprocess

# This function create pasword based on input


def generatePassword():
    password = textentry.get()
    if len(password) < 8:
        lab.grid_forget()
        cop.grid_forget()
        output.set(
            f"Your password is too short: Only {len(password)} characters.")
        out.grid()
    else:
        strongPassword = short(password)
        output.set(strongPassword)
        template()


def short(password):
    strongPassword = ""
    for symbol in password:
        if symbol == ' ':
            symbol = ''
        elif symbol == 'a':
            symbol = '@'
        elif symbol == 'l':
            symbol = '1'
        elif symbol == 'e':
            symbol = '3'
        elif symbol == 'i':
            symbol = '!'
        elif symbol == 's':
            symbol = '$'
        elif symbol == 'o':
            symbol = '0'
        elif symbol == 'p':
            symbol = '%'
        elif symbol == 'h':
            symbol = '#'
        strongPassword += symbol
    return strongPassword

# Sown output


def template():
    lab.grid(row=4)
    out.grid(row=5)
    cop.grid(row=6)

# Copy button


def copy():
    data = output.get()
    subprocess.run("pbcopy", universal_newlines=True, input=data)

# GUI


window = Tk()
window.geometry("400x250")
window.title("Strong pasword generator")
output = StringVar()
header = "This program alous you to create your personal strong password \n based on e.g \"Your Name\" and its easy to remember."
varPrompt = "Create password based on: "
window.configure(background='#ececeb')

# Information label


Label(window, text=header) .grid()
Label(window, text=varPrompt) .grid()

# Entry field


textentry = Entry(window, width=40)
textentry.grid()

# Submit Button


Button(window, text="GENERATE PASSWORD",
       width=20, command=generatePassword) .grid()

# Output


lab = Label(window, text="Your strong password is: ")
out = Label(window, textvariable=output)

# Copy button


cop = Button(window, text="COPY", width=5, command=copy,)

# Main GUI loop


window.mainloop()
