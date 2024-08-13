import csv
with open("./top_movies.csv", "r") as f:
    movies = csv.reader(f)
    
    results = [movie[0] for movie in movies if "DreamWorks" in movie]

    print(results)