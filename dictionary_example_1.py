menu_item={"cheeseburger":2.99, "small fry":0.99, "Medium Fry":1.99, "Large fry":2.99,"Milk shake":4.99, "double cheeseburger":4.99}

customer_1_item = menu_item.get("cheeseburger")
print(f"customer 1 ordered a cheeserburger for {customer_1_item}")


print(f"items of a dictionary: {menu_item.items()}")
print(f"values of a dictionary: {menu_item.values()}")
print(f"keys of a dictionary: {menu_item.keys()}")
menu_item["milk shake"]= 8.99

for key in menu_item:
    print(key)

for key, value in menu_item.items():
    print(key, value)