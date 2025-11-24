# Inventory dictionary with stock, price, and discount price
inventory = {
    "Bread": [42, 1.20, 0.99],  # "Item": [current stock, regular price, discounted price]
    "Eggs": [225, 2.12, 1.99],  # Eggs should be sold at a discount
    "Apples": [9, 1.50, 1.35]   # Apples need to be restocked
}
for i in inventory:
    #print (inventory[i][0]) 
    if inventory[i][0] < 30:
        print(f"{i} need restocking.")
    elif inventory[i][0] > 100:
        print(f"{i} should be sold at the discounted price of {inventory[i][2]}.")
    else: ## inventory[i][0] >=30 <100:
       print(f"{i} should be sold at the regular price of {inventory[i][1]}.")