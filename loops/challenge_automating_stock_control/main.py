# Initialize the inventory dictionary with stock details
inventory = {
    "Bread": [30, 50, 10, False],   # "Item": [current stock, minimum stock, restock quantity, on sale (True/False)]
    "Eggs": [120, 200, 40, False],
    "Milk": [60, 100, 20, False],
    "Apples": [15, 50, 15, False]
}

discount_threshold = 100
print ("Processing started")
for i in (inventory):
    print(f"Processing {i}")
    while inventory[i][0] <inventory[i][1]:
        inventory[i][0] += inventory[i][2]
        if inventory[i][0] > discount_threshold:
            inventory[i][3] = True
print ("Processing completed")
print(inventory)
        
