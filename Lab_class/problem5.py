number = int(input("Enter an integer greater than 1: "))

if number <= 1:
    print("Please enter an integer greater than 1.")

else:
    is_prime = True
    first_divisor = 0

    for divisor in range(2, number):
        if number % divisor == 0:
            is_prime = False
            first_divisor = divisor
            break

    if is_prime:
        print(number, "is a prime number.")
    else:
        print(
            number,
            "is not prime. Its first divisor is",
            str(first_divisor) + "."
        )
