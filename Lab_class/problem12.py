stock = {
    "pen": 25,
    "notebook": 12,
    "marker": 8
}

delivery = {
    "notebook": 10,
    "marker": 5,
    "eraser": 20
}

# Update stock using the delivery dictionary
for product, delivered_quantity in delivery.items():
    if product in stock:
        stock[product] += delivered_quantity
    else:
        stock[product] = delivered_quantity

total_items = 0

print("Updated stock:")

# Display products in alphabetical order
for product in sorted(stock):
    print(product + ":", stock[product])
    total_items += stock[product]

print("\nTotal number of items in stock:", total_items)