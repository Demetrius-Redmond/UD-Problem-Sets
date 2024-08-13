def power(num: int, power: int) -> int:
    result = num
    for x in range(1, power):
        result *= num
    print(result)
power(5,4)

