vegetables = ["tomatoes", "potatoes", "onions"]
vegetables.remove("onions")
add_carrot= "carrots" not in vegetables
#print(add_carrots)
add_cucumber="cucumbers" not in vegetables
#print(add_cucumber)
if add_carrot==True:
    vegetables.append("carrots")
else:
    print("Carrots are already in the list.")
if add_cucumber==True:
     vegetables.append("cucumbers")
else:
    print("Cucumbers are already in the list.")
vegetables.sort()
print("Updated Vegetable Inventory:", vegetables)