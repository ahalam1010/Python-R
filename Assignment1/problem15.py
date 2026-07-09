# Take a list of integers from the user and calculate sum, average, largest, and smallest.

numbers = list(map(int, input("Enter integers separated by spaces: ").split()))

total = sum(numbers)
average = total / len(numbers)
largest = max(numbers)
smallest = min(numbers)

print("List:", numbers)
print("Sum:", total)
print("Average:", average)
print("Largest value:", largest)
print("Smallest value:", smallest)