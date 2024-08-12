import string

def substitution_cipher(substitution, message):
    cipher_key = {}
    alphabet = string.ascii_uppercase
    encrypted = ""
    for i in range(len(substitution)-1):
        cipher_key[alphabet[i]] = substitution[i]
    
    for letter in message:
        encrypted += cipher_key[letter]

    return encrypted
print(substitution_cipher("YTNSHKVEFXRBAUQZCLWDMIPGJO", "HELLO"))



