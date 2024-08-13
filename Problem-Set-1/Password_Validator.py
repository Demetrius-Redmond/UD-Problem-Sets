# Write a program to check whether the provided string has at least one lower case letter, one upper case letter, one number and one symbol. It should let the user know what they are missing if they are missing something and let them know if it’s valid or if it’s invalid.

def issymbol(word: str)-> bool:
    symbols = ["~","!","@","#","$","%","^","&","*","(",")","_","-","+","=","[","]","{","}","|",";",":",",","<",".",">","/","?"]
    for letter in word:
        if letter in symbols:
            return True
    return False    
        



while True:

    lowercase = False
    uppercase = False
    numeric = False
    symbol = False

    password = input(f"Please choose a password: ")
    
    for digit in password:
        if digit.islower():
            lowercase = True
        if digit.isupper():
            uppercase = True
        if digit.isnumeric():
            numeric = True
        if issymbol(digit):
            symbol = True
        

    if lowercase and uppercase and numeric and symbol == True:
        print("Password valid")
        break
    else:
        print("Password is invalid")
        if lowercase == False:
            print("password must contain atleast 1 lower case letter.")
        if uppercase == False:
            print("password must contain atleast 1 upper case letter.")
        if numeric == False:
            print("password must contain atleast 1 number.") 
        if symbol == False:
            print("password must contain atleast 1 symbol")
        