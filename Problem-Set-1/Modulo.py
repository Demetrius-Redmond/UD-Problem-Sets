import math
def mod(num_1: int, num_2: int) -> int:
    modulo = 0
    if num_1 <= num_2:
        print(modulo)       
    else: 
        result = num_1 // num_2
        result = num_2 * result
        modulo = num_1 - result
    print(math.ceil(modulo))
mod(15, 4)

# Either my code is wrong or there's a typo on the problem set. "mod(15, 4) should result in 1"