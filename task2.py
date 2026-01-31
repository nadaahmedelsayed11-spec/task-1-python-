#Weather Advisor
temp = (float(input ("enter the temp")))
if  temp >= 30:
   print ("It's a hot day. Stay hydrated!")
elif  20 <= temp <= 29:
   print ("It's a warm day. Enjoy the weather!")
elif  10 <= temp <= 19: 
   print ("It's a cool day. Wear a jacket")
else :
   print ("It's a cold day. Stay warm!")
 #  Filter and Transform a List
 #Create a list of integers from 1 to 20
numbers = (list(range(1,21)))
print (numbers)
 #Use a for loop to find all the numbers in the list that are divisible by 3
for numb in numbers:
  if numb % 3 == 0 :
     print(f"{numb} is divisible by 3")
  else:
     print (f"{numb} is not divisible by 3")
# Print the numbers divisible by 3 (done in previous one )
print("Final list of numbers divisible by 3:")
for numb in numbers:
    if numb % 3 == 0:
        print(numb)