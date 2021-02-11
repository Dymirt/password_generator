# Main program
def main():
    print("This program alous you to create your personal strong password based on e.g \"Your Name\" and its easy to remember.")
    while True:
        password = inToString(generatePassword(
            input("Create password based on: ")))
        if len(password) < 8:
            print("Your word is too short.")
        else:
            print("Do yoou like this password?:", password)
            agrement = input("Type \"y\" for YES, or press eny key for NO: ")
            if agrement == "y":
                break
            else:
                continue
# End of main program

# This function convert list in to string
def inToString(l):
    s = ""
    for i in l:
        s += i
    return s

# This function create pasword based on input
def generatePassword(password):
    new_password = [] 
    change = None
    i = 0
    while i < len(password):
        # When Users input is longer then 11 haracter this changes make password shorter, and still easy to remember.
        if i + 3 <= len(password) and len(password) > 11:
            if password[i] == "a" and password[i + 1] == "n" and password[i + 2] == "d":
                change = "&"
                i += 3
                new_password.append(change)
            elif password[i] == "o" and password[i + 1] == "n" and password[i + 2] == "e":
                change = "1"
                i += 3
                new_password.append(change)
            elif password[i] == "f" and password[i + 1] == "o" and password[i + 2] == "r":
                change = "4"
                i += 3
                new_password.append(change)
            elif password[i] == "t" and password[i + 1] == "w" and password[i + 2] == "o":
                change = "4"
                i += 3
                new_password.append(change)
        # For all other cases
        if password[i] == " ":
            change = ""
        elif password[i] == "a" or password[i] == "A":
            change = "@"
        elif password[i] == "l" or password[i] == "L":
            change = "1"
        elif password[i] == "e" or password[i] == "E":
            change = "3"
        elif password[i] == "i" or password[i] == "I":
            change = "!"
        elif password[i] == "s" or password[i] == "S":
            change = "$"
        elif password[i] == "o" or password[i] == "O":
            change = "0"
        elif password[i] == "p" or password[i] == "P":
            change = "%"
        elif password[i] == "h" or password[i] == "H":
            change = "#"
        else:
            change = password[i]
        new_password.append(change)
        i += 1
    return new_password


# Run nain program
main()
