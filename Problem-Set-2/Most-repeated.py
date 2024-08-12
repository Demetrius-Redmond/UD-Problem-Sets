def most_repeated(array):
    array_count = {}
    for x in array:
        count = 0
        for y in array:
            if y == x:
                count += 1            
        array_count[x]=count
        
    return array_count
print(most_repeated([0,1,1,0,1,0,1,0,0]))