def min_and_max(numbers: list) -> int:
    max = 0
    for num in numbers:
        if num > max:
            max = num
    min = max
    for num in numbers:
        if num < min:
            min = num

    print(f"The min number is {min} and the max number is {max}.")

min_and_max([8, 2, 3, 10, 4])