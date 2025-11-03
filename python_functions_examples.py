"""
Python Functions - Learning Examples
=====================================
This file demonstrates:
1. Basic Function Definitions
2. Parameters and Arguments
3. Return Values
4. Default Parameters
5. Keyword Arguments
6. *args and **kwargs
7. Lambda Functions
8. Function Scope
9. Recursion
10. Built-in Functions

Run this file to see the output of each example.
"""

print("=" * 60)
print("PYTHON FUNCTIONS - COMPREHENSIVE GUIDE")
print("=" * 60)
print()

# ============================================================================
# PART 1: BASIC FUNCTION DEFINITIONS
# ============================================================================

print("PART 1: BASIC FUNCTION DEFINITIONS")
print("-" * 60)

# 1. Simple function with no parameters
print("\n1. Simple function with no parameters")


def greet():
    """A function that prints a greeting."""
    print("Hello, World!")


print("Calling greet():")
greet()

# 2. Function with parameters
print("\n2. Function with parameters")


def greet_person(name):
    """A function that greets a specific person."""
    print(f"Hello, {name}!")


print("Calling greet_person('Alice'):")
greet_person("Alice")
print("Calling greet_person('Bob'):")
greet_person("Bob")

# 3. Function with multiple parameters
print("\n3. Function with multiple parameters")


def introduce(first_name, last_name):
    """A function that introduces a person."""
    print(f"My name is {first_name} {last_name}.")


print("Calling introduce('John', 'Doe'):")
introduce("John", "Doe")

# 4. Function with return value
print("\n4. Function with return value")


def add(a, b):
    """A function that adds two numbers and returns the result."""
    result = a + b
    return result


sum_result = add(5, 3)
print(f"Calling add(5, 3): {sum_result}")


def multiply(x, y):
    """A function that multiplies two numbers."""
    return x * y


product = multiply(4, 7)
print(f"Calling multiply(4, 7): {product}")

# 5. Function that returns multiple values
print("\n5. Function that returns multiple values")


def divide_and_remainder(dividend, divisor):
    """Returns both the quotient and remainder."""
    quotient = dividend // divisor
    remainder = dividend % divisor
    return quotient, remainder


q, r = divide_and_remainder(17, 5)
print(f"Calling divide_and_remainder(17, 5):")
print(f"  Quotient: {q}, Remainder: {r}")

print("\n" + "=" * 60)

# ============================================================================
# PART 2: DEFAULT PARAMETERS
# ============================================================================

print("\nPART 2: DEFAULT PARAMETERS")
print("-" * 60)

# Functions with default parameter values
print("\n1. Functions with default parameter values")


def greet_with_message(name, message="Hello"):
    """Greets a person with an optional custom message."""
    print(f"{message}, {name}!")


print("Calling greet_with_message('Alice'):")
greet_with_message("Alice")  # Uses default message
print("Calling greet_with_message('Bob', 'Good morning'):")
greet_with_message("Bob", "Good morning")  # Uses custom message


def calculate_power(base, exponent=2):
    """Calculates base raised to exponent. Default exponent is 2."""
    return base ** exponent


print(f"\nCalling calculate_power(5): {calculate_power(5)}")  # 5^2
print(f"Calling calculate_power(5, 3): {calculate_power(5, 3)}")  # 5^3


def create_profile(name, age=18, city="Unknown"):
    """Creates a profile with optional age and city."""
    return f"Name: {name}, Age: {age}, City: {city}"


print(f"\n{create_profile('Alice')}")
print(f"{create_profile('Bob', 25)}")
print(f"{create_profile('Charlie', 30, 'New York')}")

print("\n" + "=" * 60)

# ============================================================================
# PART 3: KEYWORD ARGUMENTS
# ============================================================================

print("\nPART 3: KEYWORD ARGUMENTS")
print("-" * 60)

# Using keyword arguments
print("\n1. Using keyword arguments")


def describe_person(name, age, occupation):
    """Describes a person with their details."""
    print(f"{name} is {age} years old and works as a {occupation}.")


print("Positional arguments:")
describe_person("Alice", 25, "Engineer")

print("\nKeyword arguments:")
describe_person(name="Bob", age=30, occupation="Doctor")

print("\nMixed (positional then keyword):")
describe_person("Charlie", age=28, occupation="Teacher")

# Benefits: Order doesn't matter with keyword arguments
print("\nOrder doesn't matter with keyword arguments:")
describe_person(occupation="Artist", name="Diana", age=32)

print("\n" + "=" * 60)

# ============================================================================
# PART 4: *args AND **kwargs
# ============================================================================

print("\nPART 4: *args AND **kwargs")
print("-" * 60)

# *args - Variable number of positional arguments
print("\n1. *args - Variable number of positional arguments")


def sum_all(*args):
    """Takes any number of arguments and returns their sum."""
    total = 0
    for number in args:
        total += number
    return total


print(f"sum_all(1, 2, 3): {sum_all(1, 2, 3)}")
print(f"sum_all(1, 2, 3, 4, 5): {sum_all(1, 2, 3, 4, 5)}")
print(f"sum_all(10, 20): {sum_all(10, 20)}")


def average(*numbers):
    """Calculates the average of any number of values."""
    if len(numbers) == 0:
        return 0
    return sum(numbers) / len(numbers)


print(f"\naverage(10, 20, 30): {average(10, 20, 30)}")
print(f"average(5, 15, 25, 35, 45): {average(5, 15, 25, 35, 45)}")

# **kwargs - Variable number of keyword arguments
print("\n2. **kwargs - Variable number of keyword arguments")


def print_info(**kwargs):
    """Prints information from keyword arguments."""
    for key, value in kwargs.items():
        print(f"{key}: {value}")


print("Calling print_info(name='Alice', age=25, city='Boston'):")
print_info(name="Alice", age=25, city="Boston")


def create_student(**details):
    """Creates a student dictionary from keyword arguments."""
    student = {}
    for key, value in details.items():
        student[key] = value
    return student


student1 = create_student(name="Bob", age=20, grade="A", major="Computer Science")
print(f"\ncreate_student(name='Bob', age=20, grade='A', major='CS'):")
print(f"  {student1}")

# Combining *args and **kwargs
print("\n3. Combining *args and **kwargs")


def flexible_function(*args, **kwargs):
    """Accepts both positional and keyword arguments."""
    print("Positional arguments (*args):", args)
    print("Keyword arguments (**kwargs):", kwargs)


print("Calling flexible_function(1, 2, 3, name='Alice', age=25):")
flexible_function(1, 2, 3, name="Alice", age=25)

print("\n" + "=" * 60)

# ============================================================================
# PART 5: LAMBDA FUNCTIONS (ANONYMOUS FUNCTIONS)
# ============================================================================

print("\nPART 5: LAMBDA FUNCTIONS (ANONYMOUS FUNCTIONS)")
print("-" * 60)

# Basic lambda function
print("\n1. Basic lambda function")

# Regular function
def square(x):
    return x ** 2


# Equivalent lambda function
square_lambda = lambda x: x ** 2

print(f"Regular function square(5): {square(5)}")
print(f"Lambda function square_lambda(5): {square_lambda(5)}")

# Lambda with multiple parameters
print("\n2. Lambda with multiple parameters")

add_lambda = lambda a, b: a + b
print(f"add_lambda(3, 7): {add_lambda(3, 7)}")

# Lambda functions are often used with map, filter, and sorted
print("\n3. Using lambda with built-in functions")

numbers = [1, 2, 3, 4, 5]

# Using map with lambda
squared = list(map(lambda x: x ** 2, numbers))
print(f"Original: {numbers}")
print(f"Squared (map): {squared}")

# Using filter with lambda
even_numbers = list(filter(lambda x: x % 2 == 0, numbers))
print(f"Even numbers (filter): {even_numbers}")

# Using sorted with lambda
students = [("Alice", 25), ("Bob", 20), ("Charlie", 30)]
sorted_by_age = sorted(students, key=lambda student: student[1])
print(f"Students: {students}")
print(f"Sorted by age: {sorted_by_age}")

print("\n" + "=" * 60)

# ============================================================================
# PART 6: FUNCTION DOCSTRINGS AND DOCUMENTATION
# ============================================================================

print("\nPART 6: FUNCTION DOCSTRINGS AND DOCUMENTATION")
print("-" * 60)

# Functions with docstrings
print("\n1. Functions with docstrings")


def calculate_area(length, width):
    """
    Calculate the area of a rectangle.
    
    Args:
        length (float): The length of the rectangle
        width (float): The width of the rectangle
    
    Returns:
        float: The area of the rectangle
    """
    return length * width


area = calculate_area(5, 3)
print(f"calculate_area(5, 3): {area}")

# Accessing docstrings
print("\n2. Accessing docstrings")
print("Docstring for calculate_area:")
print(calculate_area.__doc__)

# help() function
print("\n3. Using help() function")
print("(Uncomment the next line to see help output)")
# help(calculate_area)

print("\n" + "=" * 60)

# ============================================================================
# PART 7: FUNCTION SCOPE
# ============================================================================

print("\nPART 7: FUNCTION SCOPE")
print("-" * 60)

# Global vs Local variables
print("\n1. Global vs Local variables")

global_var = "I am global"


def demonstrate_scope():
    """Demonstrates local and global scope."""
    local_var = "I am local"
    print(f"Inside function - global_var: {global_var}")
    print(f"Inside function - local_var: {local_var}")


print(f"Outside function - global_var: {global_var}")
demonstrate_scope()
# print(f"Outside function - local_var: {local_var}")  # This would cause an error

# Modifying global variables
print("\n2. Modifying global variables")

counter = 0


def increment_counter():
    """Increments a global counter variable."""
    global counter
    counter += 1
    print(f"Counter inside function: {counter}")


print(f"Counter before: {counter}")
increment_counter()
increment_counter()
print(f"Counter after: {counter}")

print("\n" + "=" * 60)

# ============================================================================
# PART 8: RECURSION
# ============================================================================

print("\nPART 8: RECURSION")
print("-" * 60)

# Factorial using recursion
print("\n1. Factorial using recursion")


def factorial(n):
    """
    Calculate factorial of n using recursion.
    factorial(n) = n * factorial(n-1)
    Base case: factorial(0) = 1
    """
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n - 1)


print(f"factorial(5): {factorial(5)}")
print(f"factorial(0): {factorial(0)}")
print(f"factorial(7): {factorial(7)}")

# Fibonacci sequence using recursion
print("\n2. Fibonacci sequence using recursion")


def fibonacci(n):
    """
    Calculate the nth Fibonacci number.
    fibonacci(0) = 0, fibonacci(1) = 1
    fibonacci(n) = fibonacci(n-1) + fibonacci(n-2)
    """
    if n <= 1:
        return n
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)


print("First 10 Fibonacci numbers:")
for i in range(10):
    print(f"fibonacci({i}) = {fibonacci(i)}")

# Recursive list sum
print("\n3. Recursive list sum")


def recursive_sum(numbers):
    """Calculate sum of a list recursively."""
    if len(numbers) == 0:
        return 0
    elif len(numbers) == 1:
        return numbers[0]
    else:
        return numbers[0] + recursive_sum(numbers[1:])


my_list = [1, 2, 3, 4, 5]
print(f"recursive_sum({my_list}): {recursive_sum(my_list)}")

print("\n" + "=" * 60)

# ============================================================================
# PART 9: PRACTICAL EXAMPLES
# ============================================================================

print("\nPART 9: PRACTICAL EXAMPLES")
print("-" * 60)

# Temperature converter
print("\n1. Temperature converter")


def celsius_to_fahrenheit(celsius):
    """Convert Celsius to Fahrenheit."""
    return (celsius * 9/5) + 32


def fahrenheit_to_celsius(fahrenheit):
    """Convert Fahrenheit to Celsius."""
    return (fahrenheit - 32) * 5/9


print(f"25°C = {celsius_to_fahrenheit(25):.2f}°F")
print(f"77°F = {fahrenheit_to_celsius(77):.2f}°C")

# Password strength checker
print("\n2. Password strength checker")


def check_password_strength(password):
    """
    Check password strength.
    Returns: 'weak', 'medium', or 'strong'
    """
    if len(password) < 6:
        return "weak"
    elif len(password) < 10:
        return "medium"
    else:
        has_upper = any(c.isupper() for c in password)
        has_lower = any(c.islower() for c in password)
        has_digit = any(c.isdigit() for c in password)
        
        if has_upper and has_lower and has_digit:
            return "strong"
        else:
            return "medium"


print(f"Password 'abc': {check_password_strength('abc')}")
print(f"Password 'password123': {check_password_strength('password123')}")
print(f"Password 'MyStr0ngP@ss': {check_password_strength('MyStr0ngP@ss')}")

# Number formatter
print("\n3. Number formatter")


def format_number(number, decimals=2, prefix="", suffix=""):
    """Format a number with specified decimal places and optional prefix/suffix."""
    formatted = f"{number:.{decimals}f}"
    return f"{prefix}{formatted}{suffix}"


print(f"format_number(1234.5678): {format_number(1234.5678)}")
print(f"format_number(1234.5678, decimals=0, prefix='$'): {format_number(1234.5678, decimals=0, prefix='$')}")
print(f"format_number(99.5, suffix='%'): {format_number(99.5, suffix='%')}")

# List operations helper
print("\n4. List operations helper")


def process_list(numbers, operation="sum"):
    """
    Process a list of numbers with different operations.
    Operations: 'sum', 'product', 'max', 'min', 'average'
    """
    if not numbers:
        return None
    
    if operation == "sum":
        return sum(numbers)
    elif operation == "product":
        result = 1
        for num in numbers:
            result *= num
        return result
    elif operation == "max":
        return max(numbers)
    elif operation == "min":
        return min(numbers)
    elif operation == "average":
        return sum(numbers) / len(numbers)
    else:
        return "Invalid operation"


test_numbers = [1, 2, 3, 4, 5]
print(f"Numbers: {test_numbers}")
print(f"Sum: {process_list(test_numbers, 'sum')}")
print(f"Product: {process_list(test_numbers, 'product')}")
print(f"Average: {process_list(test_numbers, 'average')}")
print(f"Max: {process_list(test_numbers, 'max')}")
print(f"Min: {process_list(test_numbers, 'min')}")

print("\n" + "=" * 60)

# ============================================================================
# PART 10: BUILT-IN FUNCTIONS WITH FUNCTIONS
# ============================================================================

print("\nPART 10: BUILT-IN FUNCTIONS WITH FUNCTIONS")
print("-" * 60)

# map() function
print("\n1. map() - Apply function to all items in iterable")


def double(x):
    return x * 2


numbers = [1, 2, 3, 4, 5]
doubled = list(map(double, numbers))
print(f"Original: {numbers}")
print(f"Doubled (map): {doubled}")

# Using lambda with map
doubled_lambda = list(map(lambda x: x * 2, numbers))
print(f"Doubled (map with lambda): {doubled_lambda}")

# filter() function
print("\n2. filter() - Filter items based on condition")


def is_even(x):
    return x % 2 == 0


numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
evens = list(filter(is_even, numbers))
print(f"Original: {numbers}")
print(f"Even numbers (filter): {evens}")

# Using lambda with filter
evens_lambda = list(filter(lambda x: x % 2 == 0, numbers))
print(f"Even numbers (filter with lambda): {evens_lambda}")

# sorted() with key parameter
print("\n3. sorted() with key parameter")

words = ["apple", "banana", "cherry", "date"]
sorted_by_length = sorted(words, key=len)
print(f"Original: {words}")
print(f"Sorted by length: {sorted_by_length}")

sorted_reverse = sorted(words, key=lambda x: x[::-1])  # Sort by reversed string
print(f"Sorted by reversed string: {sorted_reverse}")

print("\n" + "=" * 60)
print("END OF EXAMPLES - Happy Learning!")
print("=" * 60)

