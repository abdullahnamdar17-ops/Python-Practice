a = float (input("Enter first number: "))
b = float (input("Enter second number: "))

def add():
    return a + b

def subtract():
    return a - b

def multiply():
    return a * b

def divide():
    if b == 0:
        return "Error! Division by zero."
    else:
        return a // b


print("Select operator: +, -, *, /")
operator = input("Enter operator: ")

if operator == '+':
    print(f"{a} + {b} = {add()}")
elif operator == '-':
    print(f"{a} - {b} = {subtract()}")
elif operator == '*':
    print(f"{a} * {b} = {multiply()}")
elif operator == '/':
    print(f"{a} / {b} = {divide()}")
else:
    print("Invalid operator")