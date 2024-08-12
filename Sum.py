def sum(num: int) -> int:
    result = 0
    for str_num in str(num):
        result += int(str_num)
    print(result)
sum(624)