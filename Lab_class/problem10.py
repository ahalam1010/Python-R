prices = {
    "rice": 75.0,
    "oil": 185.0,
    "milk": 95.0,
    "eggs": 12.0
}

quantities = {
    "rice": 20,
    "oil": 10,
    "milk": 15,
    "eggs": 60
}

total_inventory_value = 0
greatest_value = 0
greatest_product = ""

print("Product-wise inventory values:")

for product in prices:
    price = prices[product]
    quantity = quantities[product]

    stock_value = price * quantity

    print(
        product.capitalize(),
        ":",
        price,
        "×",
        quantity,
        "=",
        stock_value
    )

    total_inventory_value += stock_value

    if stock_value > greatest_value:
        greatest_value = stock_value
        greatest_product = product

print("\nTotal inventory value:", total_inventory_value)

print(
    "Product with the greatest stock value:",
    greatest_product.capitalize()
)

print("Greatest stock value:", greatest_value)