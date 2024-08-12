def divisibility(num_1: int, num_2: int) -> int:
    divisible = []
    for num in range(1500, 2700):
        if num % num_1 == 0 and num % num_2 ==0:
            divisible.append(num)
    print(divisible)
divisibility(5, 7)

# This problem didn't show an example like the others to use to test my code. 