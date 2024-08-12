import csv
with open("./nba_finals.csv", "r", newline="") as f:
    nba = csv.reader(f)

    def no_cigar():
        winners = []
        losers = []
        for row in nba:
            winners.append(row[1])
            losers.append(row[2])
        no_cigar = {loser for loser in losers if loser not in winners}
        return no_cigar
    print(no_cigar())