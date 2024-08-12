import csv
with open("./nba_finals.csv", "r") as f:
    nba = csv.reader(f)

    def years_won(team):
        years = []
        for row in nba:
            if row[1] == team:
                years.append(row[0])
        return years
    print(years_won("Miami Heat"))