def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    if y != 0:
        return x / y
    else:
        return "Cannot divide by zero"

def calculator():
    print("Simple Calculator")
    print("Operations:")
    print("1. Addition")
    print("2. Subtraction")
    print("3. Multiplication")
    print("4. Division")

    # Get user input
    try:
        num1 = float(input("Enter first number: "))
        num2 = float(input("Enter second number: "))
        operation = int(input("Enter operation (1-4): "))

        # Perform calculation based on user's choice
        if operation == 1:
            result = add(num1, num2)
        elif operation == 2:
            result = subtract(num1, num2)
        elif operation == 3:
            result = multiply(num1, num2)
        elif operation == 4:
            result = divide(num1, num2)
        else:
            print("Invalid operation")
            return

        # Display the result
        print("Result: ", result)

    except ValueError:
        print("Invalid input. Please enter valid numbers.")

# Run the calculator
calculator()
