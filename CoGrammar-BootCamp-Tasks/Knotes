# Introduction to Python
# Written by Gower Campbell

# This Python script covers the fundamentals of Python programming,
# focusing on variables, casting, and input/output.

# ----------------------------------------------------------------------
# Variables
# A variable is a named container used to store data in a program.

# Syntax for Variables:
# variable_name = value

# Rules for Naming Variables:
# 1. Use snake_case (e.g., user_name) instead of spaces.
# 2. Variable names cannot start with a number or contain special characters (except underscores).
# 3. Variable names are case-sensitive (e.g., Name and name are different).

# Example:
name = "Alice"  # Stores a string
age = 25        # Stores an integer
salary = 1000.50  # Stores a float

# ----------------------------------------------------------------------
# Variable Data Types
# Python supports several data types for variables:

# 1. String (str): A sequence of characters enclosed in quotes.
# Example:
greeting = "Hello, World!"
number_str = "10"  # Note: "10" is a string, not a number.

# 2. Integer (int): A whole number without decimals.
# Example:
num1 = 10
num2 = -5

# 3. Float (float): A number with a decimal point.
# Example:
pi = 3.14
temperature = -10.5

# 4. Boolean (bool): Represents True or False.
# Example:
is_raining = True
is_sunny = False

# 5. Character (char): A single letter, number, or symbol.
# In Python, characters are treated as strings of length 1.
# Example:
first_letter = "A"
symbol = "@"

# ----------------------------------------------------------------------
# Input and Output

# Input
# The input() function is used to get user input. By default, it returns the input as a string.

# Syntax:
# variable = input("Prompt message: ")

# Example:
name = input("Enter your name: ")  # Stores user input as a string
age = input("Enter your age: ")    # Even if the user enters a number, it's stored as a string

# Output
# The print() function is used to display output to the user.

# Syntax:
# print("Message", variable)

# Example:
print("Hello,", name)  # Displays a greeting with the user's name

# ----------------------------------------------------------------------
# Casting (Type Conversion)
# Casting is the process of converting a variable from one data type to another.

# Common Casting Functions:
# 1. int(): Converts a value to an integer.
# 2. float(): Converts a value to a float.
# 3. str(): Converts a value to a string.
# 4. bool(): Converts a value to a boolean.

# Example:
number_str = "10"
number_int = int(number_str)  # Converts "10" (string) to 10 (integer)
print(number_int * 2)         # Output: 20

# Handling Input with Casting
# Since input() always returns a string, casting is often required for numerical operations.

# Example:
age = int(input("Enter your age: "))  # Converts input to an integer
salary = float(input("Enter your salary: "))  # Converts input to a float

# ----------------------------------------------------------------------
# Combining Input, Output, and Casting

# Example: Salary Calculation
# Get user input
num_days = int(input("How many days did you work this month? "))
pay_per_day = float(input("How much is your pay per day? "))

# Calculate salary
salary = num_days * pay_per_day

# Display output using string formatting
print("My salary for the month is USD: {}".format(salary))

# ----------------------------------------------------------------------
# Common Errors and Tips

# 1. TypeError:
# Occurs when you try to perform an operation on incompatible data types.
# Solution: Use casting to ensure compatible data types.

# Example:
# print("10" + 5)  # This will raise a TypeError
print(int("10") + 5)  # Correct: Outputs 15

# 2. String Repetition vs. Numerical Multiplication:
# Example:
print("10" * 2)  # Output: "1010" (string repetition)
print(int("10") * 2)  # Output: 20 (numerical multiplication)

# 3. String Formatting:
# Use {} as placeholders and the .format() method to insert variables into strings.
# Example:
print("My name is {}".format(name))

# ----------------------------------------------------------------------
# Key Takeaways
# - Variables store data and can hold different data types like strings, integers, floats, and booleans.
# - Casting is essential for converting data types, especially when working with user input.
# - Input/Output allows programs to interact with users and display results.
# - Always validate and handle user input to avoid errors.

# ----------------------------------------------------------------------
# Next Steps
# - Explore advanced string formatting with f-strings (e.g., f"My name is {name}").
# - Learn about error handling to manage invalid user input gracefully.
# - Practice combining variables, casting, and input/output in more complex programs.

# ----------------------------------------------------------------------
