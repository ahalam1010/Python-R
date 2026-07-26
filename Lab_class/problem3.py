number = int(input("Enter an integer: "))

for multiplier in range(1, 13):
    product = number * multiplier

    print(number, "*", multiplier, "=", product)