def factorials(num: int) -> int:
    result = num
    for x in range(num - 1):
        num -= 1
        result *= num
    print(result)

factorials(5)