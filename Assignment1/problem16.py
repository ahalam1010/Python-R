# Create lists using list comprehension.

numbers_1_to_20 = [number for number in range(1, 21)]
even_numbers = [number for number in range(1, 21) if number % 2 == 0]
odd_numbers = [number for number in range(1, 21) if number % 2 != 0]
squares = [number ** 2 for number in range(1, 11)]

print("Numbers from 1 to 20:", numbers_1_to_20)
print("Even numbers from 1 to 20:", even_numbers)
print("Odd numbers from 1 to 20:", odd_numbers)
print("Squares of numbers from 1 to 10:", squares)