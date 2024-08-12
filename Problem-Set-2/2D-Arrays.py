def number_of_0s(array):
    count = 0
    for x in array:
        for y in x:
            if y == 0:
                count += 1
    return count
print(number_of_0s([[0,1,1],[0,1,0],[1,0,0]]))





