print("Welcome to the python learning class")
try:
    a = int(input("enter your first number:"))
    b = int(input("enter your second number:"))
    result = a / b
    print("The division of the two number is",result)
except ZeroDivisionError:
    print("Division by zero")