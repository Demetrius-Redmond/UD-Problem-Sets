# Write a program that replaces all of the following letters with the corresponding numbers (ignoring case):

leet_speak =   {"l":"1", "a":"6", "e":"3", "i":"1", "o":"0", "t":"7"}
# For example, leetSpeaK = 1337SP36K and hello WORLD = h3110 W0R1D.

phrase = input("Input: ")
output= ""


for letter in phrase:
    if letter.lower() in leet_speak:
        output += leet_speak[letter.lower()]
    else:
        output += letter
print(output)

