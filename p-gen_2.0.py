from tkinter import *


# This function create pasword based on input
def generatePassword():
    password = textentry.get()
    password = password.upper()
    new_password = []
    change = None
    i = 0
    while i < len(password):
        # When Users input is longer then 11 haracter this changes make password shorter, and still easy to remember.
        if i + 3 <= len(password) and len(password) > 11:
            if password[i] == "O" and password[i + 1] == "N" and password[i + 2] == "E":
                change = "1"
                i += 3
                new_password.append(change)
            elif password[i] == "F" and password[i + 1] == "O" and password[i + 2] == "R":
                change = "4"
                i += 3
                new_password.append(change)
            elif password[i] == "T" and password[i + 1] == "W" and password[i + 2] == "O":
                change = "2"
                i += 3
                new_password.append(change)
        if i >= len(password):
            break
        # For all other cases
        if password[i] == " ":
            change = ""
        elif password[i] == "A":
            change = "@"
        elif password[i] == "L":
            change = "1"
        elif password[i] == "E":
            change = "3"
        elif password[i] == "I":
            change = "!"
        elif password[i] == "S":
            change = "$"
        elif password[i] == "O":
            change = "0"
        elif password[i] == "P":
            change = "%"
        elif password[i] == "H":
            change = "#"
        else:
            change = password[i]
        new_password.append(change)
        i += 1

    # Convert list in to string
    strongPassword = ""
    for i in new_password:
        strongPassword += i
    strongPassword += " "
    output.insert(END, strongPassword)


window = Tk()
window.title("Title of program")
window.geometry("400x250")
window.title("Strong pasword generator")

# Information label
Label(window, text="This program alous you to create your personal strong password \n based on e.g \"Your Name\" and its easy to remember.") .grid(row=0, column=0)
Label(window, text="Create password based on: ") .grid(row=1, column=0)
# Entry field
textentry = Entry(window, width=40)
textentry.grid(row=2, column=0)
# Submit Button
Button(window, text="GENERATE PASSWORD", width=20, highlightbackground="Black", command=generatePassword,) .grid(row=3, column=0)
# Output
Label(window, text="Your strong password is: ") .grid(row=4, column=0)
output = Text(window, width=50, height=1)
output.grid(row=5, column=0)

window.mainloop()