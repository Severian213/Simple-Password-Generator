from random import randrange
SYMBOL_SET = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890'

def symbolSet(symSet):
    '''Ask a user if they want to add special characters to the standard symbol set.'''
    print("The standard set of characters used to generate passwords contains the letters\n\
a through z in lowercase and uppercase, and the numbers 0 to 9. It is recommended\n\
that you add special characters to this set.")
    specialOrNot = input("\nType 'y' to add special characters, type 'n' to continue with the standard set: ")
    if specialOrNot.startswith('y'):
        specialChars = input("Please enter the special characters you want to use: ")
    else:
        return symSet
    for i in specialChars:
        if i not in symSet:
            if i == ' ':
                print("You can't have a space in a password!")
            else:    
                symSet += i
        else:
            print(f"{i} is already in the symbol set")
    return symSet

def howManyPasswords():
    while True:
        try:
            numOfPasswords = int(input("How many passwords would you like to generate? ")) # Get the user to input how many passwords they want generated.
        except ValueError:
            print("Please enter an integer.")
            continue
        else:
            break

    return numOfPasswords

def charactersPerPassword():
    '''Get the user to input how many characters they want in each password.'''
    while True:
        try:
            passChar = int(input("How many characters do you want in each password? ")) # Get the user to input how many characters they want in each password
        except ValueError:
            print("Please enter an integer.")
            continue
        else:
            break

    return passChar


def passwordGeneration(numOfPasswords, passChar, SYMBOL_SET):
    if numOfPasswords > 1:
        print("\nHere are your passwords:")
    else:
        print("\nHere is your password:")
        
    for i in range(numOfPasswords):
        password = ''
        for e in range(passChar):
            password += SYMBOL_SET[randrange(len(SYMBOL_SET))]
        print(f"{password}")

symbols = symbolSet(SYMBOL_SET)
numOfPasswords = howManyPasswords()
passChar = charactersPerPassword()
passwordGeneration(numOfPasswords, passChar, symbols)

input("\nPress Enter to exit.")


