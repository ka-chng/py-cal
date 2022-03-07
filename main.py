
# Addition
def add(x, y):
    return x + y

# Subtraction
def subtract(x, y):
    return x - y

# Multiplication
def multiply(x, y):
    return x * y

# Divison
def divide(x, y):
    return x / y

print("Select from one of the options below")
print("\033[1;34;40m [1] Addition")
print("\033[1;34;40m [2] Subtraction")
print("\033[1;34;40m [3] Multiplication")
print("\033[1;34;40m [4] Division")

while True:
    # Take input from the user
    choice = input("Select an option [1, 2, 3, 4] ")

    # Check if choice is one of the four options
    if choice in ('1', '2', '3', '4'):
        num1 = float(input("Enter first number: "))
        num2 = float(input("Enter second number: "))

        if choice == '1':
            print(num1, "+", num2, "=", add(num1, num2))

        elif choice == '2':
            print(num1, "-", num2, "=", subtract(num1, num2))

        elif choice == '3':
            print(num1, "*", num2, "=", multiply(num1, num2))

        elif choice == '4':
            print(num1, "/", num2, "=", divide(num1, num2))
        
        # Checks if user wants another calculation
        # Breaks the while loop if the user does not want to
        next_calculation = input("To end this program reply with no, otherwise yes to make another caluclation")
        if next_calculation == "no":
          break

    else:
        print("Invalid input")