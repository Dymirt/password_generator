# Main program
#
def main():
    password = inToString(generatePassword(input("Create password based on word: ")))
    if len(password) < 8:
        print("Your word is too short.")
    else:
        print(password)

# This function convert list in to string
# 
def inToString(l):
    s = ""
    for i in l:
        s += i
    return s
# This function create pasword based on input
#
def generatePassword(password):
    new_password = []
    for item in password:
        if item == " ":
            item = "" 
        elif item == "l":
            item = "1"
        elif item == "e" or item == "E":
            item = "3"
        elif item == "s" or item == "S":
            item = "$"
        elif item == "o" or item == "O":
            item = "0"
        elif item.islower():
            item = item.upper()
        elif item.isupper():
            item = item.lower()
        
        new_password.append(item)
    return new_password
main()