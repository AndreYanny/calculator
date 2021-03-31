# Program make a simple calculator

# This function adds two numbers
def add(x, y):
    print(x, "+", y, "=", x + y)


# This function subtracts two numbers
def subtract(x, y):
    print(x, "-", y, "=", x - y)


# This function multiplies two numbers
def multiply(x, y):
    print(x, "*", y, "=", x * y)


# This function divides two numbers
def divide(x, y):
    try:
        print(x, "/", y, "=", x / y)
    except ZeroDivisionError:
        print("Division by zero error!")


print("Select operation.")
print("1.Add")
print("2.Subtract")
print("3.Multiply")
print("4.Divide")

while True:
    # Take input from the user
    choice = input("\nEnter choice(1/2/3/4): ")

    # Check if choice is one of the four options
    if choice in ('1', '2', '3', '4'):
        num1 = float(input("Enter first number: "))
        num2 = float(input("Enter second number: "))

        if choice == '1':
            add(num1, num2)

        elif choice == '2':
            subtract(num1, num2)

        elif choice == '3':
            multiply(num1, num2)

        elif choice == '4':
            divide(num1, num2)
        break
    else:
        print("Invalid Input")
