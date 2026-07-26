n = int(input("Enter a nonnegative integer n: "))

if n < 0:
    print("Factorial is not defined for negative integers.")

elif n == 0:
    print("0! = 1")

else:
    factorial = 1

    for number in range(1, n + 1):
        factorial *= number

        if number < n:
            print(number, end=" * ")
        else:
            print(number, end=" = ")

    print(factorial)