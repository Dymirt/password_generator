# Main program
#
def main():
    print("This program alous you to create your personal strong password based on e.g \"Your Name\" and its easy to remember.")
    while True:
        password = inToString(generatePassword(
            input("Create password based on: ")))
        if len(password) < 8:
            print("Your word is too short.")
        else:
            print("Try this password:", password)
            break

# This function convert list in to string


def inToString(l):
    s = ""
    for i in l:
        s += i
    return s

# This function create pasword based on input


def generatePassword(password):
    new_password = []
    for item in password:
        if item == " ":
            item = ""
        elif item == "a" or item == "A":
            item = "@"
        elif item == "l" or item == "L":
            item = "1"
        elif item == "e" or item == "E":
            item = "3"
        elif item == "i" or item == "I":
            item = "!"
        elif item == "s" or item == "S":
            item = "$"
        elif item == "o" or item == "O":
            item = "0"
        elif item == "p" or item == "P":
            item = "%"
        elif item.islower():
            item = item.upper()
        elif item.isupper():
            item = item.lower()

        new_password.append(item)
    return new_password


main()
