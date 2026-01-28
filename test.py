#task 1 
#Defi#ne variables for the prices of three items
product1 = 100
product2 = 200
product3 = 300 
#Define a variable for the total budget
budget = 700 
#Calculate the total cost of the items
totalcost  = product1 + product2 + product3 
#Compare the total cost with the budget
if budget>=totalcost:
 print("enoughf")
 balance = budget - totalcost
 print(f"{balance}")
else:
 print("notenoughf")
 needed = totalcost - budget
 print("{needed}")
#Calculate the difference 
