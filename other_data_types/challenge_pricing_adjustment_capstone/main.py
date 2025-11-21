grocery_inventory={"Milk": ("Dairy", 3.50, 8),"Eggs": ("Dairy", 5.50, 30),"Bread": ("Bakery", 2.99, 15),"Apples": ("Produce", 1.50, 50)}
egg_info = grocery_inventory.get("Eggs")
milk_info = grocery_inventory.get("Milk")
apple_info = grocery_inventory.get("Apples")
egg_price = egg_info[1]
#print(egg_price)
if egg_price > 5:
    print ("Eggs are too expensive, reducing the price by $1.")
    egg_price = egg_price - 1.00
    grocery_inventory.update ({"Eggs":("Dairy", egg_price, 30)})
    #print(egg_price)
else:
    print ("The price of Eggs is reasonable.")
grocery_inventory.update({"Tomatoes":("Produce", 1.20, 30)})
print ("Inventory after adding Tomatoes:", grocery_inventory)
milk_stock = milk_info[2]
#print (milk_stock)
if milk_stock < 10:
    print("Milk needs to be restocked.  Increasing stock by 20 units.")
    milk_stock = milk_stock + 20
    grocery_inventory.update({"Milk":("Dairy", 3.50, milk_stock)})
    #print (milk_stock)
else:
    print("Milk has sufficient stock.")
apple_price = apple_info[1]
#print (apple_price)
if apple_price > 2:
    grocery_inventory.pop("Apples")
    print ("Apples removed from inventory due to high price.")
print ("Updated inventory:", grocery_inventory)