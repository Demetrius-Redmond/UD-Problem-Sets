with open("./countries.txt", "r") as file:
    countries = file.read().splitlines()
    
VOWELS = ["a", "e", "i", "o", "u"]


def united()-> list[str]:
    results = []
    for country in countries:
        if "United" in country:
            results.append(country)
    return results
# print(united())

def begin_end_with_vowel()-> list[str]:
    results = []
    for country in countries:
        # Tried to put both if statments in one line using and...
        if country[0].lower() in VOWELS:
            if country[-1].lower() in VOWELS:
                results.append(country)
    return results
# print(begin_end_with_vowel())

def over_half_vowels():
    # Not sure if this is corret
    
    for country in countries:
        vowel_count = 0
        for x in country:
            if x.lower() in VOWELS:
                vowel_count += 1
        results = [country for country in countries if len(country) // 2 > vowel_count]
        
    return results
# print(over_half_vowels())

def shortest_country_name():
    shortest = countries[0]
    results = []
    for country in countries:
        if len(country) < len(shortest):
            shortest = country
    results = [country for country in countries if len(country) == len(shortest)]
    return results
# print(shortest_country_name())


def one_vowel():
    vowels = VOWELS    
    results = []
    for country in countries:
        found_vowel = []
        omit = "no"
        for letter in country:
            if letter.lower() in vowels:
                found_vowel.append(letter.lower())
            
        for letter in found_vowel:
            if len(found_vowel) == 1:
                continue
            elif letter != found_vowel[0]:
                omit = "yes"
        if omit == "no":
            results.append(country) 
        
    return results
# print(one_vowel())
 


def contains_name():
    results = []
    for country in countries:
        for country_2 in countries:
            if country in country_2 and country != country_2:
                results.append(country_2)
    return results
# print(contains_name())

for country in countries:
    print(country)