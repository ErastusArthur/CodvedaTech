def add(a,b):
    return a + b
def subtract(a,b):
    return a - b
def multiply(a,b):
    return a * b
def divide(a,b):
    if b == 0:
        return "Error! Division by zero."
    return a / b

operations = {
    "1": ("Add", add),
    "2": ("Subtract", subtract),
    "3": ("Multiply", multiply),
    "4": ("Divide", divide)
}
while True:
    print("""
Select an operation:
1. Add
2. Subtract
3. Multiply
4. Divide
""")
    choice = input("Enter your choice(1/2/3/4) or 'e' to exit: ").lower()

    if choice == 'e':
        print("It was nice to have you with us! Goodbye for now.")
        break
    if choice in operations:
        try:
            num1 = float(input("Enter your first number: "))
            num2 = float(input("Enter your second number: "))
            name, func = operations[choice]
            result = func(num1, num2)
            print(f"Your result is: {result}")
        except ValueError:
            print("Invalid input. Please try again with a valid number.")
    else:
        print("Invalid choice. Please try again.")

