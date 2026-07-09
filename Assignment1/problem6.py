numbers = [10, 20, 30, 40, 50, 60]

search_number = int(input("Enter a number to search: "))

found = False

for i in range(len(numbers)):
    if numbers[i] == search_number:
        print("Number exists in the list.")
        print("Position/index:", i)
        found = True
        break

if not found:
    print("Number does not exist in the list.")