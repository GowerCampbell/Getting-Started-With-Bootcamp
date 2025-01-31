
# Variables and Data Types in Python

Variables are the building blocks of any programming language. In this section, you'll learn how to declare variables, understand different data types, and use them effectively in your Python programs.

## Table of Contents
1. [What is a Variable?](#what-is-a-variable)
2. [Declaring Variables](#declaring-variables)
3. [Data Types in Python](#data-types-in-python)
   - [Strings](#strings)
   - [Integers](#integers)
   - [Floats](#floats)
   - [Booleans](#booleans)
4. [Variable Naming Rules](#variable-naming-rules)
5. [Practical Examples](#practical-examples)
6. [Next Steps](#next-steps)

## What is a Variable?
A variable is a named container that stores data. Think of it as a label you attach to a value so you can reuse it later in your program. For example:

```python
name = "Gower"
age = 25
```

Here:

- `name` is a variable storing the string "Gower".
- `age` is a variable storing the integer 25.

## Declaring Variables
In Python, you declare a variable by assigning a value to it using the `=` operator. Python automatically detects the data type based on the value you assign.

Example:

```python
# Declaring variables
name = "Alice"  # String
age = 30        # Integer
height = 5.5    # Float
is_student = True  # Boolean
```

## Data Types in Python
Python supports several built-in data types. Here are the most common ones:

### Strings
- Used to store text.
- Enclosed in single (`'`) or double (`"`) quotes.

Example:

```python
greeting = "Hello, World!"
```

### Integers
- Used to store whole numbers.
- No decimal points.

Example:

```python
age = 25
```

### Floats
- Used to store decimal numbers.

Example:

```python
pi = 3.14
```

### Booleans
- Used to store True or False values.

Example:

```python
is_student = True
```

## Variable Naming Rules
When naming variables, follow these rules:

- Start with a letter or underscore (`_`).
- Use only letters, numbers, and underscores.
- Avoid Python keywords (e.g., `print`, `input`).
- Use descriptive names (e.g., `user_name` instead of `x`).

### Example of good variable names:

```python
user_name = "Alice"
user_age = 30
```

### Example of bad variable names:

```python
1name = "Alice"  # Starts with a number
user-name = "Alice"  # Contains a hyphen
```

## Practical Examples

### Example 1: Storing and Displaying Data

```python
# Declare variables
name = "Gower"
age = 25

# Display the values
print("Name:", name)
print("Age:", age)
```

**Output:**
```
Name: Gower
Age: 25
```

### Example 2: Combining Variables

```python
# Declare variables
first_name = "Alice"
last_name = "Smith"

# Combine variables
full_name = first_name + " " + last_name
print("Full Name:", full_name)
```

**Output:**
```
Full Name: Alice Smith
```

## Next Steps
Now that you understand variables and data types, you can explore:

- **Casting and Type Conversion** - Learn how to convert between data types.
- **Input and Output** - Get user input and display output in your programs.

Ready to move forward? Let’s dive into Casting and Type Conversion! 🚀


