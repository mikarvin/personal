"""
Python Flow Control - Learning Examples
=======================================
This file demonstrates:
1. Conditional Statements (if, elif, else)
2. Comparison and Logical Operators
3. For Loops
4. While Loops
5. Nested Loops
6. Break and Continue Statements
7. Loop Control with Else
8. Pass Statement
9. Practical Examples

Run this file to see the output of each example.
"""

print("=" * 60)
print("PYTHON FLOW CONTROL - COMPREHENSIVE GUIDE")
print("=" * 60)
print()

# ============================================================================
# PART 1: CONDITIONAL STATEMENTS (if, elif, else)
# ============================================================================

print("PART 1: CONDITIONAL STATEMENTS (if, elif, else)")
print("-" * 60)

# 1. Simple if statement
print("\n1. Simple if statement")

temperature = 25
if temperature > 20:
    print(f"Temperature is {temperature}°C - It's warm!")

temperature = 15
if temperature > 20:
    print(f"Temperature is {temperature}°C - It's warm!")
else:
    print(f"Temperature is {temperature}°C - It's cool!")

# 2. if-else statement
print("\n2. if-else statement")

age = 18
if age >= 18:
    print(f"Age {age}: You are an adult.")
else:
    print(f"Age {age}: You are a minor.")

age = 16
if age >= 18:
    print(f"Age {age}: You are an adult.")
else:
    print(f"Age {age}: You are a minor.")

# 3. if-elif-else statement
print("\n3. if-elif-else statement")

score = 85
if score >= 90:
    grade = "A"
elif score >= 80:
    grade = "B"
elif score >= 70:
    grade = "C"
elif score >= 60:
    grade = "D"
else:
    grade = "F"

print(f"Score {score}: Grade {grade}")

score = 95
if score >= 90:
    grade = "A"
elif score >= 80:
    grade = "B"
elif score >= 70:
    grade = "C"
elif score >= 60:
    grade = "D"
else:
    grade = "F"

print(f"Score {score}: Grade {grade}")

score = 55
if score >= 90:
    grade = "A"
elif score >= 80:
    grade = "B"
elif score >= 70:
    grade = "C"
elif score >= 60:
    grade = "D"
else:
    grade = "F"

print(f"Score {score}: Grade {grade}")

# 4. Nested if statements
print("\n4. Nested if statements")

age = 25
has_license = True

if age >= 18:
    if has_license:
        print(f"Age {age} with license: You can drive!")
    else:
        print(f"Age {age} without license: You need a license first.")
else:
    print(f"Age {age}: You are too young to drive.")

print("\n" + "=" * 60)

# ============================================================================
# PART 2: COMPARISON AND LOGICAL OPERATORS
# ============================================================================

print("\nPART 2: COMPARISON AND LOGICAL OPERATORS")
print("-" * 60)

# 1. Comparison operators in conditionals
print("\n1. Comparison operators in conditionals")

x = 10
y = 5

if x == y:
    print(f"{x} == {y}: True")
else:
    print(f"{x} == {y}: False")

if x != y:
    print(f"{x} != {y}: True")

if x > y:
    print(f"{x} > {y}: True")

if x < y:
    print(f"{x} < {y}: True")
else:
    print(f"{x} < {y}: False")

if x >= y:
    print(f"{x} >= {y}: True")

if x <= y:
    print(f"{x} <= {y}: True")
else:
    print(f"{x} <= {y}: False")

# 2. Logical operators (and, or, not)
print("\n2. Logical operators (and, or, not)")

age = 25
has_ticket = True

if age >= 18 and has_ticket:
    print(f"Age {age} and has ticket: You can enter!")

age = 15
has_ticket = True

if age >= 18 and has_ticket:
    print(f"Age {age} and has ticket: You can enter!")
else:
    print(f"Age {age} and has ticket: Cannot enter (too young).")

# Using 'or'
age = 25
has_ticket = False
is_vip = True

if age >= 18 or is_vip:
    print(f"Age {age}, ticket: {has_ticket}, VIP: {is_vip}: You can enter!")

# Using 'not'
is_raining = False

if not is_raining:
    print("It's not raining - Perfect weather for a walk!")

# 3. Multiple conditions
print("\n3. Multiple conditions")

temperature = 25
is_sunny = True
is_weekend = True

if temperature > 20 and is_sunny and is_weekend:
    print("Perfect day for a picnic!")

temperature = 15
if temperature > 20 and is_sunny and is_weekend:
    print("Perfect day for a picnic!")
else:
    print("Maybe not the best day for a picnic.")

# Complex conditions
age = 20
has_license = True
has_insurance = True

if age >= 18 and has_license and has_insurance:
    print("You can drive legally!")
elif age >= 18 and has_license:
    print("You have a license but need insurance.")
elif age >= 18:
    print("You need a license first.")
else:
    print("You're too young to drive.")

print("\n" + "=" * 60)

# ============================================================================
# PART 3: FOR LOOPS
# ============================================================================

print("\nPART 3: FOR LOOPS")
print("-" * 60)

# 1. Basic for loop with range()
print("\n1. Basic for loop with range()")

print("Counting from 0 to 4:")
for i in range(5):
    print(f"  i = {i}")

print("\nCounting from 1 to 5:")
for i in range(1, 6):
    print(f"  i = {i}")

print("\nCounting by 2s from 0 to 8:")
for i in range(0, 10, 2):
    print(f"  i = {i}")

# 2. For loop with lists
print("\n2. For loop with lists")

fruits = ["apple", "banana", "orange", "grape"]
print("Iterating through fruits list:")
for fruit in fruits:
    print(f"  I like {fruit}")

# 3. For loop with index using enumerate()
print("\n3. For loop with index using enumerate()")

fruits = ["apple", "banana", "orange"]
print("Iterating with index:")
for index, fruit in enumerate(fruits):
    print(f"  Index {index}: {fruit}")

# 4. For loop with strings
print("\n4. For loop with strings")

word = "Python"
print(f"Iterating through string '{word}':")
for letter in word:
    print(f"  {letter}")

# 5. For loop with dictionaries
print("\n5. For loop with dictionaries")

student = {"name": "Alice", "age": 20, "grade": "A"}
print("Iterating through dictionary keys:")
for key in student:
    print(f"  {key}: {student[key]}")

print("\nUsing .items():")
for key, value in student.items():
    print(f"  {key}: {value}")

print("\nUsing .values():")
for value in student.values():
    print(f"  Value: {value}")

# 6. Nested for loops
print("\n6. Nested for loops")

print("Multiplication table (2x2):")
for i in range(1, 3):
    for j in range(1, 3):
        print(f"  {i} x {j} = {i * j}")

print("\n" + "=" * 60)

# ============================================================================
# PART 4: WHILE LOOPS
# ============================================================================

print("\nPART 4: WHILE LOOPS")
print("-" * 60)

# 1. Basic while loop
print("\n1. Basic while loop")

count = 0
print("Counting from 0 to 4:")
while count < 5:
    print(f"  count = {count}")
    count += 1

# 2. While loop with condition
print("\n2. While loop with condition")

number = 10
print(f"Starting number: {number}")
print("Dividing by 2 until number < 1:")
while number >= 1:
    print(f"  number = {number}")
    number = number / 2

# 3. While loop with user input simulation
print("\n3. While loop with counter")

attempts = 0
max_attempts = 3
password = "secret123"
correct = False

print("Password guessing simulation:")
while attempts < max_attempts and not correct:
    attempts += 1
    print(f"  Attempt {attempts}: Trying password...")
    if attempts == 2:  # Simulate correct password on 2nd attempt
        correct = True
        print(f"  Attempt {attempts}: Password correct!")

if correct:
    print("  Access granted!")
else:
    print("  Access denied - too many attempts!")

# 4. Infinite loop prevention
print("\n4. While loop with break (avoiding infinite loops)")

counter = 0
print("Counting with break condition:")
while True:
    counter += 1
    print(f"  counter = {counter}")
    if counter >= 5:
        print("  Breaking out of loop!")
        break

print("\n" + "=" * 60)

# ============================================================================
# PART 5: BREAK AND CONTINUE STATEMENTS
# ============================================================================

print("\nPART 5: BREAK AND CONTINUE STATEMENTS")
print("-" * 60)

# 1. Break statement
print("\n1. Break statement - exiting loop early")

print("Finding first number divisible by 7:")
for i in range(1, 20):
    if i % 7 == 0:
        print(f"  Found: {i}")
        break
    print(f"  Checking {i}...")

# 2. Continue statement
print("\n2. Continue statement - skipping iteration")

print("Printing even numbers from 1 to 10:")
for i in range(1, 11):
    if i % 2 != 0:  # Skip odd numbers
        continue
    print(f"  {i} is even")

# 3. Break in nested loops
print("\n3. Break in nested loops")

print("Finding first pair where sum equals 10:")
found = False
for i in range(1, 6):
    for j in range(1, 6):
        if i + j == 10:
            print(f"  Found: {i} + {j} = 10")
            found = True
            break
    if found:
        break

# 4. Continue in nested loops
print("\n4. Continue in nested loops")

print("Printing pairs where both numbers are even:")
for i in range(1, 6):
    if i % 2 != 0:
        continue
    for j in range(1, 6):
        if j % 2 != 0:
            continue
        print(f"  ({i}, {j})")

print("\n" + "=" * 60)

# ============================================================================
# PART 6: LOOP CONTROL WITH ELSE
# ============================================================================

print("\nPART 6: LOOP CONTROL WITH ELSE")
print("-" * 60)

# 1. For loop with else
print("\n1. For loop with else")

print("Searching for number 5 in range(1, 5):")
for i in range(1, 5):
    if i == 5:
        print(f"  Found {i}!")
        break
else:
    print("  5 not found in range!")

print("\nSearching for number 3 in range(1, 5):")
for i in range(1, 5):
    if i == 3:
        print(f"  Found {i}!")
        break
else:
    print("  3 not found in range!")

# 2. While loop with else
print("\n2. While loop with else")

number = 10
print(f"Checking if {number} is prime (simple check):")
divisor = 2
while divisor < number:
    if number % divisor == 0:
        print(f"  {number} is divisible by {divisor} - not prime")
        break
    divisor += 1
else:
    print(f"  {number} appears to be prime (no divisors found)")

print("\n" + "=" * 60)

# ============================================================================
# PART 7: PASS STATEMENT
# ============================================================================

print("\nPART 7: PASS STATEMENT")
print("-" * 60)

# 1. Pass as placeholder
print("\n1. Pass as placeholder")

age = 25
if age >= 18:
    pass  # Placeholder - will implement later
else:
    print("Too young!")

# 2. Pass in loops
print("\n2. Pass in loops")

for i in range(5):
    if i % 2 == 0:
        pass  # Do nothing for even numbers
    else:
        print(f"  Odd number: {i}")

# 3. Pass in function definitions
print("\n3. Pass in function definitions")

def future_function():
    """Function to be implemented later."""
    pass

print("Function defined with pass - no implementation yet")

print("\n" + "=" * 60)

# ============================================================================
# PART 8: PRACTICAL EXAMPLES
# ============================================================================

print("\nPART 8: PRACTICAL EXAMPLES")
print("-" * 60)

# 1. Number guessing game logic
print("\n1. Number guessing game logic")

secret_number = 7
guesses = [3, 5, 7, 9]
print(f"Secret number: {secret_number}")
print("Guessing:")

for guess in guesses:
    if guess == secret_number:
        print(f"  Guess {guess}: Correct! You win!")
        break
    elif guess < secret_number:
        print(f"  Guess {guess}: Too low!")
    else:
        print(f"  Guess {guess}: Too high!")

# 2. Finding maximum in a list
print("\n2. Finding maximum in a list")

numbers = [3, 7, 2, 9, 1, 5]
print(f"List: {numbers}")

max_value = numbers[0]
for num in numbers:
    if num > max_value:
        max_value = num

print(f"Maximum value: {max_value}")

# 3. Filtering even numbers
print("\n3. Filtering even numbers")

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
even_numbers = []

for num in numbers:
    if num % 2 == 0:
        even_numbers.append(num)

print(f"Original list: {numbers}")
print(f"Even numbers: {even_numbers}")

# 4. Sum of numbers until negative
print("\n4. Sum of numbers until negative")

numbers = [5, 10, 3, 8, -2, 7, 4]
print(f"Numbers: {numbers}")
total = 0
count = 0

for num in numbers:
    if num < 0:
        print(f"  Negative number encountered: {num}")
        break
    total += num
    count += 1

print(f"Sum of numbers before negative: {total}")
print(f"Numbers processed: {count}")

# 5. Temperature classification
print("\n5. Temperature classification")

temperatures = [15, 25, 30, 5, 35, 10, 20]
print("Classifying temperatures:")
for temp in temperatures:
    if temp >= 30:
        category = "Hot"
    elif temp >= 20:
        category = "Warm"
    elif temp >= 10:
        category = "Cool"
    else:
        category = "Cold"
    print(f"  {temp}°C: {category}")

# 6. Password validation
print("\n6. Password validation")

passwords = ["abc", "password123", "MyStr0ngP@ss", "short"]
print("Validating passwords:")

for password in passwords:
    is_valid = True
    if len(password) < 8:
        is_valid = False
        print(f"  '{password}': Too short (need at least 8 characters)")
    elif not any(c.isupper() for c in password):
        is_valid = False
        print(f"  '{password}': Missing uppercase letter")
    elif not any(c.islower() for c in password):
        is_valid = False
        print(f"  '{password}': Missing lowercase letter")
    elif not any(c.isdigit() for c in password):
        is_valid = False
        print(f"  '{password}': Missing digit")
    else:
        print(f"  '{password}': Valid password!")

# 7. Counting occurrences
print("\n7. Counting occurrences")

numbers = [1, 2, 3, 2, 4, 2, 5, 2, 6]
target = 2
print(f"List: {numbers}")
print(f"Counting occurrences of {target}:")

count = 0
for num in numbers:
    if num == target:
        count += 1

print(f"  {target} appears {count} times")

# 8. Building a list with conditions
print("\n8. Building a list with conditions")

numbers = list(range(1, 21))
print(f"Original numbers: {numbers}")

squares_of_evens = []
for num in numbers:
    if num % 2 == 0:
        squares_of_evens.append(num ** 2)

print(f"Squares of even numbers: {squares_of_evens}")

# 9. Finding first prime number (simple check)
print("\n9. Finding first prime number (simple check)")

numbers = [4, 6, 7, 8, 9, 10, 11]
print(f"Numbers: {numbers}")
print("Finding first prime number:")

for num in numbers:
    is_prime = True
    if num < 2:
        is_prime = False
    else:
        for i in range(2, num):
            if num % i == 0:
                is_prime = False
                break
    
    if is_prime:
        print(f"  First prime found: {num}")
        break
else:
    print("  No prime numbers found!")

# 10. Menu simulation
print("\n10. Menu simulation")

choice = 3  # Simulating menu choice
print("Menu options:")
print("  1. Option 1")
print("  2. Option 2")
print("  3. Option 3")
print(f"Selected choice: {choice}")

if choice == 1:
    print("  Executing Option 1...")
elif choice == 2:
    print("  Executing Option 2...")
elif choice == 3:
    print("  Executing Option 3...")
else:
    print("  Invalid choice!")

print("\n" + "=" * 60)

# ============================================================================
# PART 9: ADVANCED PATTERNS
# ============================================================================

print("\nPART 9: ADVANCED PATTERNS")
print("-" * 60)

# 1. List comprehension alternative (showing loop equivalent)
print("\n1. Loop equivalent of list comprehension")

numbers = [1, 2, 3, 4, 5]
squared = []
for num in numbers:
    squared.append(num ** 2)
print(f"Original: {numbers}")
print(f"Squared (using loop): {squared}")

# 2. Pattern printing
print("\n2. Pattern printing with nested loops")

print("Printing triangle pattern:")
for i in range(1, 6):
    print("  " + "*" * i)

# 3. Processing multiple lists
print("\n3. Processing multiple lists")

names = ["Alice", "Bob", "Charlie"]
ages = [25, 30, 28]
print("Combining names and ages:")
for i in range(len(names)):
    print(f"  {names[i]} is {ages[i]} years old")

# Using zip()
print("\nUsing zip() for parallel iteration:")
for name, age in zip(names, ages):
    print(f"  {name} is {age} years old")

# 4. Conditional list building
print("\n4. Conditional list building")

numbers = list(range(1, 16))
print(f"Numbers: {numbers}")

fizzbuzz_results = []
for num in numbers:
    if num % 15 == 0:
        fizzbuzz_results.append("FizzBuzz")
    elif num % 3 == 0:
        fizzbuzz_results.append("Fizz")
    elif num % 5 == 0:
        fizzbuzz_results.append("Buzz")
    else:
        fizzbuzz_results.append(str(num))

print("FizzBuzz results:")
for i, result in enumerate(fizzbuzz_results[:10], 1):
    print(f"  {i}: {result}")

print("\n" + "=" * 60)
print("END OF FLOW CONTROL EXAMPLES - Happy Learning!")
print("=" * 60)

