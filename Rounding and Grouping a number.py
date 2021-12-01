"""Rounding off a value to two decimal places and also group them into thousands"""

def main():
    balance = 2000000.56789
    return f'This converts to {balance:,.2f}'


print(main())
