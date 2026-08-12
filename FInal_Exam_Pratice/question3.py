inventory = {
    "P101": {
        "name": "Keyboard",
        "stock": 8,
        "reorder_level": 10,
        "unit_price": 1500
    },

    "P102": {
        "name": "Mouse",
        "stock": 15,
        "reorder_level": 12,
        "unit_price": 800
    },

    "P103": {
        "name": "Headset",
        "stock": 4,
        "reorder_level": 8,
        "unit_price": 2200
    },

    "P104": {
        "name": "Webcam",
        "stock": 6,
        "reorder_level": 6,
        "unit_price": 3000
    }
}


def create_reorder_list(items):
    reorder_list = []

    for code, info in items.items():
        if info["stock"] < info["reorder_level"]:
            order_quantity = (2 * info["reorder_level"]) - info["stock"]
            cost = order_quantity * info["unit_price"]

            reorder_list.append({
                "code": code,
                "name": info["name"],
                "order_quantity": order_quantity,
                "cost": cost
            })
    return reorder_list

reorder = create_reorder_list(inventory)

for item in reorder:
    print(
        "Code: ", item["code"],
        "Name:", item["name"],
        "Quantity:", item["order_quantity"],
        "Cost:", item["cost"],

    )

total = 0

total_cost = 0

for item in reorder:
    total_cost += item["cost"]

print("Total Cost:", total_cost)