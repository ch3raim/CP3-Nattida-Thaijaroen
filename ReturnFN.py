def vatCalculate(price):
    total = price+(price*7/100)
    return total

price = int(input("INPUT Price : "))
print(vatCalculate(price))