given = [-5, -4, -3, -2, -1, 0, 1, 2, 3, 4, 5]

user = int(input("Enter a number: "))

if user in given:
    print(f"The number {user} is in the list {given}")

    for i in range(len(given)):
        if given[i] == user:
            print(f"The index of the number {user} is: {i}")


else:
    print(f"The number {user} is not in the list {given}")

