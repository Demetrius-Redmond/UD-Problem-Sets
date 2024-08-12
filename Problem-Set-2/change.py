from decimal import Decimal


def change_calculator(change:float):
    money = {
    "$20 bill": "20",
    "$10 bill" : "10",
    "$5 bill" : "5",
    "$1 bill" : "1",
    "quarter" : ".25",
    "dime" : ".10",
    "nickel" : ".05",
    "penny" : ".01",
    }

    deduct = str(change)
    deduct = Decimal(deduct)


    for currency in money:
        amount = 0
        while deduct - Decimal(money[currency]) >= 0:
            amount += 1
            deduct -= Decimal(money[currency])
            # printing to show what is returned
            
        if amount > 1:
            print(f"{amount} {currency}s")
        elif amount > 0:
            print(f"{amount} {currency}")

change_calculator(.41)