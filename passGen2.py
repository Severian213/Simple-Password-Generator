# Import the necessary modules
import secrets
import string

# Create the symbol set the user requires
def symbolSet():
    '''Ask a user if they want to add special characters to the standard symbol set.'''
    SYMBOL_SET = string.ascii_letters + string.digits
    print("The standard set of characters used to generate passwords contains the letters\n\
a through z in lowercase and uppercase, and the numbers 0 to 9. It is recommended\n\
that you add special characters to this set.")
    specialOrNot = input("\nEnter 'y' to add special characters, press any other key to continue with the standard set: ")
    # added .lower() to handle more cases. 
    if specialOrNot.lower().startswith('y'):
        while True:
            specialChars = input("Please enter the special characters you want to use: ")
            
            # Separate valid and invalid characters
            validChars = ''.join(x for x in specialChars if x in string.printable)
            invalidChars = ''.join(x for x in specialChars if x not in string.printable)

            if invalidChars:
                print(f"Invalid characters removed: {invalidChars}")

            SYMBOL_SET += validChars
            break
    
    return SYMBOL_SET

def howManyPasswords():
    '''Get the user to input how many passwords they want generated. '''
    # This function has been tidied up slightly. The continue key word has been removed in the except block.
    # the else block now simply returns 'numOfPasswords'
    while True:
        try:
            numOfPasswords = int(input("How many passwords would you like to generate? ")) # Get the user to input how many passwords they want generated.
        except ValueError:
            print("Please enter an integer.")
        else:
            return numOfPasswords
        
def charactersPerPassword():
    '''Get the user to input how many characters they want in each password.'''
    while True:
        try:
            passChar = int(input("How many characters do you want in each password? ")) # Get the user to input how many characters they want in each password
        except ValueError:
            print("Please enter an integer.")
        else:
            return passChar


def passwordGeneration(numOfPasswords, passChar, SYMBOL_SET):
    if numOfPasswords > 1:
        print("\nHere are your passwords:")
    else:
        print("\nHere is your password:")
        
    for i in range(numOfPasswords):
        password = ''.join(secrets.choice(SYMBOL_SET) for x in range(passChar))
        print(password)
        

def main():
    symbols = symbolSet()
    numOfPasswords = howManyPasswords()
    passChar = charactersPerPassword()
    passwordGeneration(numOfPasswords, passChar, symbols)

    input("\nPress Enter to exit.")

if __name__ == '__main__':
    main()