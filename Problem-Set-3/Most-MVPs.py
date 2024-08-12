import csv
with open("./nba_finals.csv", "r") as f:
   
    nba = csv.reader(f)

    def most_mvp():
        winners = [] 
        results = {}  
        for row in nba:
            if row[4] != "":
                winners.append(row[4]) 
        mvp = {name for name in winners}
          
        for name in mvp: 
            x = 0
            for name_count in winners:
                if name_count == name:
                    x += 1
            if x > 1:        
                results[name] = x
        
        return sorted(results.items(), key=lambda x:x[1], reverse=True)
    # I don't understand what the lambda is doing here. I assume lambda x == x[1] aka x = results and 1 = the value but if that's true shouldn't 1 be index 0?
    print(most_mvp())
    

    