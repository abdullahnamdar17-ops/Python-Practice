try:
    x = int(input("Enter valur of x: "))
    print("Value of x is: ", x)
except ValueError:
    print("Invalid input! Please enter an integer.")