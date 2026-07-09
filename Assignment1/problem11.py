# Sort a list in ascending and descending order using sort().

numbers = [45, 12, 78, 3, 25, 90]

ascending_order = numbers.copy()
ascending_order.sort()

descending_order = numbers.copy()
descending_order.sort(reverse=True)

print("Original list:", numbers)
print("Ascending order:", ascending_order)
print("Descending order:", descending_order)