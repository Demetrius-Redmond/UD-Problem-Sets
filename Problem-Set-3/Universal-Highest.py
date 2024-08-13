import csv
with open("./top_movies.csv", "r") as f:
    movies = csv.reader(f)

    
    universal = [movie for movie in movies if "Universal" in movie[1]]

    gross = []
    for movie in universal:
        gross.append(int(movie[3]))
    for movie in universal:
        if int(movie[3]) == max(gross):
            print(movie)
           
            