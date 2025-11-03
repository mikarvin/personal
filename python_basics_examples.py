"""
Python Basics - Learning Examples
==================================
This file demonstrates:
1. Basic Python Data Types
2. Basic Python Operations

Run this file to see the output of each example.
"""

print("=" * 60)
print("PYTHON BASICS - DATA TYPES AND OPERATIONS")
print("=" * 60)
print()

# ============================================================================
# PART 1: BASIC PYTHON DATA TYPES
# ============================================================================

print("PART 1: BASIC PYTHON DATA TYPES")
print("-" * 60)

# 1. INTEGER (int) - Whole numbers
print("\n1. INTEGER (int) - Whole numbers")
age = 25
temperature = -10
big_number = 1000000
print(f"age = {age}, type: {type(age)}")
print(f"temperature = {temperature}, type: {type(temperature)}")
print(f"big_number = {big_number}, type: {type(big_number)}")

# 2. FLOAT - Decimal numbers
print("\n2. FLOAT - Decimal numbers")
height = 5.9
pi = 3.14159
price = 19.99
print(f"height = {height}, type: {type(height)}")
print(f"pi = {pi}, type: {type(pi)}")
print(f"price = {price}, type: {type(price)}")

# 3. STRING (str) - Text data
print("\n3. STRING (str) - Text data")
name = "Alice"
greeting = 'Hello, World!'
multiline = """This is a
multi-line string"""
print(f"name = {name}, type: {type(name)}")
print(f"greeting = {greeting}, type: {type(greeting)}")
print(f"multiline = {multiline}")

# 4. BOOLEAN (bool) - True or False
print("\n4. BOOLEAN (bool) - True or False")
is_student = True
is_graduated = False
print(f"is_student = {is_student}, type: {type(is_student)}")
print(f"is_graduated = {is_graduated}, type: {type(is_graduated)}")

# 5. LIST - Ordered, mutable collection
print("\n5. LIST - Ordered, mutable collection")
fruits = ["apple", "banana", "orange"]
numbers = [1, 2, 3, 4, 5]
mixed = [1, "hello", 3.14, True]
print(f"fruits = {fruits}, type: {type(fruits)}")
print(f"numbers = {numbers}, type: {type(numbers)}")
print(f"mixed = {mixed}, type: {type(mixed)}")

# 6. TUPLE - Ordered, immutable collection
print("\n6. TUPLE - Ordered, immutable collection")
coordinates = (10, 20)
colors = ("red", "green", "blue")
print(f"coordinates = {coordinates}, type: {type(coordinates)}")
print(f"colors = {colors}, type: {type(colors)}")

# 7. DICTIONARY (dict) - Key-value pairs
print("\n7. DICTIONARY (dict) - Key-value pairs")
person = {
    "name": "Bob",
    "age": 30,
    "city": "New York"
}
grades = {"math": 95, "science": 88, "english": 92}
print(f"person = {person}, type: {type(person)}")
print(f"grades = {grades}, type: {type(grades)}")

# 8. SET - Unordered, unique elements
print("\n8. SET - Unordered, unique elements")
unique_numbers = {1, 2, 3, 4, 5}
vowels = {"a", "e", "i", "o", "u"}
print(f"unique_numbers = {unique_numbers}, type: {type(unique_numbers)}")
print(f"vowels = {vowels}, type: {type(vowels)}")

# 9. NONE - Represents absence of value
print("\n9. NONE - Represents absence of value")
result = None
print(f"result = {result}, type: {type(result)}")

print("\n" + "=" * 60)

# ============================================================================
# PART 2: BASIC PYTHON OPERATIONS
# ============================================================================

print("\nPART 2: BASIC PYTHON OPERATIONS")
print("-" * 60)

# ARITHMETIC OPERATIONS
print("\n1. ARITHMETIC OPERATIONS")
a = 10
b = 3

print(f"a = {a}, b = {b}")
print(f"Addition (a + b): {a + b}")
print(f"Subtraction (a - b): {a - b}")
print(f"Multiplication (a * b): {a * b}")
print(f"Division (a / b): {a / b}")
print(f"Floor Division (a // b): {a // b}")  # Returns integer part
print(f"Modulus (a % b): {a % b}")  # Returns remainder
print(f"Exponentiation (a ** b): {a ** b}")  # a to the power of b

# COMPARISON OPERATIONS
print("\n2. COMPARISON OPERATIONS")
x = 5
y = 8

print(f"x = {x}, y = {y}")
print(f"Equal (x == y): {x == y}")
print(f"Not Equal (x != y): {x != y}")
print(f"Less Than (x < y): {x < y}")
print(f"Greater Than (x > y): {x > y}")
print(f"Less Than or Equal (x <= y): {x <= y}")
print(f"Greater Than or Equal (x >= y): {x >= y}")

# LOGICAL OPERATIONS
print("\n3. LOGICAL OPERATIONS")
p = True
q = False

print(f"p = {p}, q = {q}")
print(f"AND (p and q): {p and q}")
print(f"OR (p or q): {p or q}")
print(f"NOT (not p): {not p}")
print(f"NOT (not q): {not q}")

# STRING OPERATIONS
print("\n4. STRING OPERATIONS")
first_name = "John"
last_name = "Doe"

# Concatenation
full_name = first_name + " " + last_name
print(f"Concatenation: '{first_name}' + ' ' + '{last_name}' = '{full_name}'")

# Repetition
dashes = "-" * 5
print(f"Repetition: '-' * 5 = '{dashes}'")

# String methods
text = "  Hello, World!  "
print(f"Original: '{text}'")
print(f"Upper: '{text.upper()}'")
print(f"Lower: '{text.lower()}'")
print(f"Strip (remove spaces): '{text.strip()}'")
print(f"Replace: '{text.replace('World', 'Python')}'")
print(f"Find 'World': {text.find('World')}")
print(f"Length: {len(text)}")

# String indexing and slicing
word = "Python"
print(f"\nString: '{word}'")
print(f"First character (word[0]): '{word[0]}'")
print(f"Last character (word[-1]): '{word[-1]}'")
print(f"Slicing (word[0:2]): '{word[0:2]}'")
print(f"Slicing (word[2:]): '{word[2:]}'")
print(f"Reverse (word[::-1]): '{word[::-1]}'")

# LIST OPERATIONS
print("\n5. LIST OPERATIONS")
numbers = [1, 2, 3]
print(f"Original list: {numbers}")

# Adding elements
numbers.append(4)
print(f"After append(4): {numbers}")

numbers.insert(0, 0)
print(f"After insert(0, 0): {numbers}")

# Removing elements
numbers.remove(2)
print(f"After remove(2): {numbers}")

popped = numbers.pop()
print(f"After pop(): {numbers}, popped value: {popped}")

# List slicing
numbers = [0, 1, 2, 3, 4, 5]
print(f"\nList: {numbers}")
print(f"First 3 elements: {numbers[0:3]}")
print(f"Last 2 elements: {numbers[-2:]}")
print(f"Every other element: {numbers[::2]}")

# List methods
numbers = [3, 1, 4, 1, 5, 9, 2, 6]
print(f"\nList: {numbers}")
print(f"Length: {len(numbers)}")
print(f"Sum: {sum(numbers)}")
print(f"Max: {max(numbers)}")
print(f"Min: {min(numbers)}")
print(f"Sorted: {sorted(numbers)}")
print(f"Count of 1: {numbers.count(1)}")
print(f"Index of 4: {numbers.index(4)}")

# DICTIONARY OPERATIONS
print("\n6. DICTIONARY OPERATIONS")
student = {"name": "Alice", "age": 20, "grade": "A"}
print(f"Dictionary: {student}")

# Accessing values
print(f"Name: {student['name']}")
print(f"Age: {student.get('age')}")
print(f"City (with default): {student.get('city', 'Not specified')}")

# Adding/Updating
student["city"] = "Boston"
student["age"] = 21
print(f"After adding/updating: {student}")

# Removing
removed_grade = student.pop("grade")
print(f"After pop('grade'): {student}, removed: {removed_grade}")

# Dictionary methods
print(f"Keys: {student.keys()}")
print(f"Values: {student.values()}")
print(f"Items: {student.items()}")

# SET OPERATIONS
print("\n7. SET OPERATIONS")
set1 = {1, 2, 3, 4}
set2 = {3, 4, 5, 6}
print(f"set1: {set1}")
print(f"set2: {set2}")

print(f"Union (set1 | set2): {set1 | set2}")
print(f"Intersection (set1 & set2): {set1 & set2}")
print(f"Difference (set1 - set2): {set1 - set2}")
print(f"Symmetric Difference (set1 ^ set2): {set1 ^ set2}")

# Adding to set
set1.add(5)
print(f"After add(5): {set1}")

set1.remove(1)
print(f"After remove(1): {set1}")

# MEMBERSHIP OPERATIONS
print("\n8. MEMBERSHIP OPERATIONS")
my_list = [1, 2, 3, 4, 5]
my_string = "Hello"
my_dict = {"a": 1, "b": 2}

print(f"3 in {my_list}: {3 in my_list}")
print(f"'e' in '{my_string}': {'e' in my_string}")
print(f"'a' in {my_dict}: {'a' in my_dict}")
print(f"10 not in {my_list}: {10 not in my_list}")

# TYPE CONVERSION
print("\n9. TYPE CONVERSION")
num_str = "123"
num_int = int(num_str)
print(f"String '{num_str}' to int: {num_int}, type: {type(num_int)}")

num_float = float(num_int)
print(f"Int {num_int} to float: {num_float}, type: {type(num_float)}")

back_to_str = str(num_float)
print(f"Float {num_float} back to string: '{back_to_str}', type: {type(back_to_str)}")

# Boolean conversion
print(f"bool(1): {bool(1)}")
print(f"bool(0): {bool(0)}")
print(f"bool('hello'): {bool('hello')}")
print(f"bool(''): {bool('')}")
print(f"bool([]): {bool([])}")
print(f"bool([1, 2]): {bool([1, 2])}")

print("\n" + "=" * 60)
print("END OF EXAMPLES - Happy Learning!")
print("=" * 60)

