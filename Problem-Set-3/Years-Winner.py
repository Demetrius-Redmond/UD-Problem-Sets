import csv

with open("./nba_finals.csv", "r") as f:
    nba = csv.reader(f)
        
    def years_winner(year):
        for row in nba:
            if row[0] == year:
                return row[1]
    print(years_winner("1956"))
    
