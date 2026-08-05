fruits = ["apple", "banana", "mango", "orange", "grapes"]

fruits.append("kiwi")
print("Append: ", fruits)

fruits.insert(0, "lemon")
print("Insert: ", fruits)

fruits.remove("banana")
print("Removed: ", fruits)

fruits.pop(1)
print("Pop: ", fruits)

fruits.clear()
print("Clear:", fruits)

fruits = ["apple", "banana", "mango", "orange", "grapes"]

new_fruit = fruits.copy()
print("Copy:", new_fruit)
