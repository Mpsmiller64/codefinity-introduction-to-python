meat = ["Ham", 3.99, 50, "Sliced"]
cheese = ["Cheddar", 5.49, 100, "Sharp"]
condiment = ["Mustard", 1.99, 75, "Spicy"]
##create main list
deli_dept = [meat, cheese, condiment]
print("Initial Deli List:", deli_dept)
##check for restock
if deli_dept[0][0]=="Ham" and deli_dept[0][2]< 100:
    deli_dept[0][2]=100
    #restock=True
print("Updated Deli List:",deli_dept)
##Add seasonal meat
seasonal_meat=["Turkey",4.50, 100, "Sliced"]
deli_dept.append(seasonal_meat)
print("Updated Deli List:",deli_dept)
deli_dept.remove(condiment)
print("Updated Deli List:",deli_dept)
deli_dept.sort()
print("Updated Deli List:",deli_dept)