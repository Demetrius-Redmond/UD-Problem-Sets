# def multiple(num_1: int, num_2: int) -> int:
#     result = 0
#     if num_1 or num_2 == 0:
#         result = 0
#     elif num_1 or num_2 == 1:
#         result = max(num_1, num_2)    
#     else:
#         for x in range(num_2):         
#             result += num_1       
#     print(result)

# multiple(4, 2)
# The else statement didn't seem to work and I don't know why and would like to understand it fully. 


def multiple(num_1: int, num_2: int) -> int:
    result = 0
    if num_1 or num_2 == 0:
        result = 0
    
    elif num_1 or num_2 == 1:
        result = max(num_1, num_2)
        
    for x in range(num_2):        
        result += num_1
                       
    print(result)

# multiple(3, 2)


