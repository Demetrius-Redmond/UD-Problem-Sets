with open("./baby-names-2020.txt", "r") as file_1:
    names = file_1.read().splitlines()

def shortest_name():
    shortest = names[0]

    for name in names:
        if len(name) < len(shortest):
            shortest = name
    return shortest
# print(shortest_name())


def longest_name():
    longest = names[0]
    results = []
    for name in names:
        if len(name) > len(longest):
            longest = name
    for name in names:
        if len(name) == len(longest):
            results.append(name)
    return results
# print(longest_name())


def word_when_backwards():
    pass
    # Liam spelled backwards is mail but as now not sure how to check for words in python. 
  
