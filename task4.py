#Prime Number Checker
def is_prime (n) :
   if n<2 :
       return False 
   for i in range(2, n):
       if n%i ==0 :
         return False
   return True 
#Custom Calculator
#Write a function calculator(a, b, operation) that takes two numbers
#and a string ("add", "subtract", "multiply", or "divide") and
#performs the respective operation.
def calculator(a, b, operation):
    if operation == "add":
        return a + b
    elif operation == "subtract":
        return a - b
    elif operation == "multiply":
        return a * b
    elif operation == "divide":
        if b == 0:
            return "Error: Cannot divide by zero!"
        return a / b
   