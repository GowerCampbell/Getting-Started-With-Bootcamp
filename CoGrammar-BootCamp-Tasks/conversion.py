# Task 2: Casting or Type Conversion
# Written by Gower Campbell

# In this task, we will explore how to convert variables from one data type to another using Python's built-in casting functions:
# - int(): Converts to integer
# - float(): Converts to float
# - str(): Converts to string

# ----------------------------------------------------------------------
# 1. Using int() to convert a Float to an Integer

# Declare a float variable
float1 = 99.23

# Convert the float to an integer
int_value = int(float1)

# Explanation:
# The int() function removes the decimal part of the float, effectively truncating it.
# This means 99.23 becomes 99.

print("1. Converting float to integer:")
print(f"Original float: {float1}")
print(f"Converted integer: {int_value}")  # Output: 99
print("Note: The decimal part is removed during conversion.\n")

# ----------------------------------------------------------------------
# 2. Using float() to convert an Integer to a Float

# Declare an integer variable
num2 = 23

# Convert the integer to a float
float_value = float(num2)

# Explanation:
# The float() function adds a decimal point to the integer, converting it to a floating-point number.
# This means 23 becomes 23.0.

print("2. Converting integer to float:")
print(f"Original integer: {num2}")
print(f"Converted float: {float_value}")  # Output: 23.0
print("Note: A decimal point is added during conversion.\n")

# ----------------------------------------------------------------------
# 3. Using str() to convert an Integer to a String

# Declare an integer variable
num3 = 150

# Convert the integer to a string
str_value = str(num3)

# Explanation:
# The str() function converts the integer into a string of characters.
# This means 150 becomes "150".

print("3. Converting integer to string:")
print(f"Original integer: {num3}")
print(f"Converted string: {str_value}")  # Output: "150"
print("Note: The number is now a sequence of characters.\n")

# ----------------------------------------------------------------------
# 4. Using int() to convert a String to an Integer

# Declare a string variable
string4 = "100"

# Convert the string to an integer
int_value_from_str = int(string4)

# Explanation:
# The int() function converts a string of numeric characters into an integer.
# This means "100" becomes 100.

print("4. Converting string to integer:")
print(f"Original string: {string4}")
print(f"Converted integer: {int_value_from_str}")  # Output: 100
print("Note: The string must contain valid numeric characters for this to work.\n")

# ----------------------------------------------------------------------
# Additional Notes:
# - Casting is useful when you need to ensure data is in the correct format for calculations or operations.
# - Be cautious when converting strings to numbers. If the string contains non-numeric characters, it will raise a ValueError.
# Example of an invalid conversion:
# invalid_string = "abc"
# int(invalid_string)  # This will raise a ValueError

# ----------------------------------------------------------------------
