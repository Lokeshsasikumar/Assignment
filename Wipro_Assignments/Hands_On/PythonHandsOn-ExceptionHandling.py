
# Exercise 1: Handle division by zero
try:
    num1 = float(input("Enter the first number: "))
    num2 = float(input("Enter the second number: "))
    result = num1 / num2
except ZeroDivisionError:
    print("Error: Cannot divide by zero.")
else:
    print(f"The result is: {result}")

# Exercise 2: Handle invalid input
try:
    num = int(input("Enter a number: "))
except ValueError:
    print("Error: Invalid input, please enter a valid number.")
else:
    print(f"You entered: {num}")


# Exercise 3: Open a file and handle exceptions
try:
    filename = input("Enter the file name: ")
    with open(filename, 'r') as file:
        print(file.read())
except FileNotFoundError:
    print(f"Error: The file '{filename}' was not found.")
except Exception as e:
    print(f"An unexpected error occurred: {e}")

# Exercise 4: Combine multiple except blocks for different errors
try:
    value = input("Enter a number: ")
    num = float(value)
    result = 10 / num
except ValueError:
    print("Error: Invalid input, please enter a valid number.")
except ZeroDivisionError:
    print("Error: Cannot divide by zero.")
else:
    print(f"Result is: {result}")


# Exercise 5: Use try-except-else-finally
try:
    num = float(input("Enter a number: "))
    result = num / 2
except Exception as e:
    print(f"Error: {e}")
else:
    print(f"The result is: {result}")
finally:
    print("Execution complete.")


# Exercise 6: Create a custom exception for negative numbers
class NegativeNumberError(Exception):
    pass

try:
    num = float(input("Enter a positive number: "))
    if num < 0:
        raise NegativeNumberError("Number cannot be negative.")
except NegativeNumberError as e:
    print(f"Error: {e}")
else:
    print(f"You entered: {num}")


# Exercise 7: Function raising ValueError if input is not between 1 and 100
def check_number(number):
    if number < 1 or number > 100:
        raise ValueError("Number must be between 1 and 100.")
    return number

try:
    num = float(input("Enter a number between 1 and 100: "))
    check_number(num)
except ValueError as e:
    print(f"Error: {e}")
else:
    print(f"You entered: {num}")

# Exercise 8: Function raising TypeError if input is not a string
def check_string(value):
    if not isinstance(value, str):
        raise TypeError("Input must be a string.")
    return value

try:
    input_value = input("Enter a string: ")
    check_string(input_value)
except TypeError as e:
    print(f"Error: {e}")
else:
    print(f"You entered: {input_value}")


# Exercise 9: Simple calculator with exception handling
def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    if y == 0:
        raise ZeroDivisionError("Cannot divide by zero.")
    return x / y

def calculator():
    try:
        num1 = float(input("Enter first number: "))
        operation = input("Enter operation (+, -, *, /): ")
        num2 = float(input("Enter second number: "))
        
        if operation == "+":
            print(f"Result: {add(num1, num2)}")
        elif operation == "-":
            print(f"Result: {subtract(num1, num2)}")
        elif operation == "*":
            print(f"Result: {multiply(num1, num2)}")
        elif operation == "/":
            print(f"Result: {divide(num1, num2)}")
        else:
            raise ValueError("Unsupported operation.")
    
    except ValueError as e:
        print(f"Error: {e}")
    except ZeroDivisionError as e:
        print(f"Error: {e}")
    except Exception as e:
        print(f"Unexpected error: {e}")

calculator()
