# Kaffine = { (𝑎,𝑏) ∈ ℤ𝑛×ℤ𝑛 | gcd(𝑎,𝑛)=1 }


# define the variable n --> length of the alphabet
n = 27

# define  the alphabet as a dictionary having the (key, value) = ('letter', 'integer value from [0,26]')
alphabet = {
    ' ': 0, 'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5, 'f': 6, 'g': 7, 'h': 8, 'i': 9, 'j': 10, 'k': 11, 'l': 12,
    'm': 13,
    'n': 14, 'o': 15, 'p': 16, 'q': 17, 'r': 18, 's': 19, 't': 20, 'u': 21, 'v': 22, 'w': 23, 'x': 24, 'y': 25,
    'z': 26
}

# define the alphabet as a string (the indexes are integer numbers)
alphabet2 = " abcdefghijklmnopqrstuvwxyz"


# We are computing the euler function to find the GDC between 2 numbers
def euler_function(a, b):
    while b > 0:
        r = a % b
        a = b
        b = r
    return a


# This function is used to print the menu
def print_menu():
    print("Affine cipher - Lab1 Cryptography\n")
    print("Select a command\n")
    print("\t\t1. Encrypt the plaintext\n")
    print("\t\t2. Decrypt the ciphertext\n")
    print("\t\t3. Exit \n")


# This function is used to encode the plain text
def encode(plainText, a, b):
    # in the beginning the plain text is an empty list
    plainTextDigits = []

    # it computes the encoded value for each letter
    # alphabet[x] will be the integer value from the dictionary having the key = x ( x is a letter from the text)
    for x in plainText:
        # appedns to the plainTextDigits list the encoded values
        plainTextDigits.append((a * alphabet[x] + b) % n)

    # after computing everything, we will have a list of integers
    # we are printing the list just to have a clear view
    print(plainTextDigits)

    # We have to change the numbers to a real text (using the codes from the dictionary)
    cipherText = ""
    for x in plainTextDigits:
        cipherText += alphabet2[x]

    # The function returns the cipherText
    return cipherText


# This function is used to validate the plainText (it has to be formed only with those 27 characters
# defined in the alphabet dictionary
def plainText_validation(plainText):
    for x in plainText:
        if x not in alphabet.keys() or x == '.':
            return 0
    return 1


# This function is used to decode the cipherText with the key
def decode(cipher, a, b):
    # It uses the same logic as the one from encode function
    # first we init an emplty list
    plainTextDigits = []

    # we are computing the inverse of a => a^(-1)
    inverse = -1
    for y in range(0, len(alphabet)):
        if (y * a) % n == 1:
            inverse = y
            break

    print(inverse)

    # it computes the decoded value for each letter
    # alphabet[x] will be the integer value from the dictionary having the key = x ( x is a letter from the cipher)
    for x in cipher:
        plainTextDigits.append((inverse * (alphabet[x] - b)) % n)

    # after computing everything, we will have a list of integers
    # we are printing the list just to have a clear view
    print(plainTextDigits)
    decodedText = ""

    # We have to change the numbers to a real text (using the codes from the dictionary)
    for x in plainTextDigits:
        decodedText += alphabet2[x]

    # The function returns the decodedText
    return decodedText


def encodeUI():
    print("The key should have 2 parts: a and b (INTEGER)")
    try:
        a = int(input("Select 'a' for the key formula: "))
        # we check if the a value is correct using the euler function
        r = euler_function(a, n)
        if r != 1 or a >= 27:
            while r != 1 or a >= 27:
                print("Choose another value for 'a'!!!")
                a = int(input("Select 'a' for the key formula "))
                r = euler_function(a, n)
        # if r != 1 or a >= 27:
        #     print("Choose another value for 'a'!!! (LESS THAN 27)")
        #     a = int(input("Select 'a' for the key formula "))
    # if it's not, we throw an error and we will ask the user to enter a valid value
    except ValueError:
        print("Choose another value for 'a'!!! (INTEGER)")
        a = int(input("Select 'a' for the key formula: "))

    # the same with b, except that we don't need euler function no more
    try:
        b = int(input("Select 'b' for the key formula: "))
        if b >= 10000:
            print("Choose another value for 'b'!!!")
            b = int(input("Select 'b' for the key formula: "))
    except ValueError:
        print("Choose another value for 'b'!!! (INTEGER)")
        b = int(input("Select 'b' for the key formula: "))

    # We are asking the user to enter the cipher and it has to be a valid one
    plainText = input("Insert the plaintext: ")
    if plainText_validation(plainText.lower()) == 0:
        print("Choose another value for plain text! You can choose only valid letters (no digits, no special chars")
        plainText = input("Insert the plaintext again: ")

    # we call the function for encoding the plainText
    cipher = encode(plainText.lower(), a, b)
    # we print the cipherText
    print(cipher.upper())


def decodeUI():
    print("The key should have 2 parts: a and b (INTEGER)")
    try:
        a = int(input("Select 'a' for the key formula: "))
        # we check if the a value is correct using the euler function
        r = euler_function(a, n)
        if r != 1 or a >= 27:
            while r != 1 or a >= 27:
                print("Choose another value for 'a'!!!")
                a = int(input("Select 'a' for the key formula "))
                r = euler_function(a, n)
    # if it's not, we throw an error and we will ask the user to enter a valid value
    except ValueError:
        print("Choose another value for 'a'!!! (INTEGER)")
        a = int(input("Select 'a' for the key formula: "))

    # the same with b, except that we don't need euler function no more
    try:
        b = int(input("Select 'b' for the key formula: "))
        if b >= 10000:
            print("Choose another value for 'b'!!!")
            b = int(input("Select 'b' for the key formula: "))
    except ValueError:
        print("Choose another value for 'b'!!! (INTEGER)")
        b = int(input("Select 'b' for the key formula: "))

    # We are asking the user to enter the cipher and it has to be a valid one
    cipher = input("Insert the cipher: ")
    if plainText_validation(cipher.lower()) == 0:
        # else we will ask to enter the value again
        print("Choose another value for  cipher! You can choose only valid letters (no digits, no special chars)")
        cipher = input("Insert the cipher again: ")

    # we call the function for decoding the cipher
    decodedText = decode(cipher.lower(), a, b)
    # we print the decodedText
    print(decodedText.upper())


def exitUI():
    print("Bye!")


# Here we have a function to handle our options
def menu_functions(i):
    switcher = {
        1: encodeUI,
        2: decodeUI,
        3: exitUI
    }
    func = switcher.get(i, lambda: 'Invalid')
    return func()


# This is the main function (the entery point of the program)
if __name__ == '__main__':
    # call of the function print_menu
    print_menu()
    # choose a command
    cmd = int(input("Choose a command: "))
    n = 27
    # depending on the command inserted, we call the menu_functions with a different param
    while cmd != 3:
        if cmd == 1:
            menu_functions(1)
        if cmd == 2:
            menu_functions(2)
        if cmd == 3:
            menu_functions(3)
            break
        print_menu()
        cmd = int(input("Choose a command: "))
