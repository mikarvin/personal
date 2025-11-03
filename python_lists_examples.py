# ===========================================================
# PYTHON BASICS IIIa – LISTS (FULL SUMMARY)
# ===========================================================

print("=" * 60)
print("PYTHON LISTS - EXAMPLES AND OUTPUT")
print("=" * 60)

# 1. Concept
# A list is a built-in data type in Python that stores a collection of items.
# Lists are ordered, mutable (can be changed), and can contain different types of data.

# Example of creating lists:
whales = [5, 4, 7, 3, 2, 3, 2, 6, 4, 2, 1, 7, 1, 3]
empty_list = []
mixed = [1, "Hello", True, 3.5]
nested = [[1, 2, 3], [4, 5, 6]]

print("Initial lists:")
print(f"  whales: {whales}")
print(f"  empty_list: {empty_list}")
print(f"  mixed: {mixed}")
print(f"  nested: {nested}")

# -----------------------------------------------------------

# 2. Accessing Elements (Indexing)
# Indexing starts from 0. Negative indices count from the end (-1 = last).
print(whales[0])   # first element
print(whales[5])   # sixth element
print(whales[-1])  # last element
# Accessing out of range index will cause IndexError

# -----------------------------------------------------------

# 3. Accessing Multiple Elements (Slicing)
# Syntax: list[start:end] - start is inclusive, end is exclusive
print(whales[2:5])   # elements at positions 2, 3, 4
print(whales[:3])    # first three
print(whales[5:])    # from index 5 to the end
print(whales[2:2])   # empty list []

# -----------------------------------------------------------

# 4. Modifying Lists (Mutability)
# Lists can be changed in place.
whales[0] = 10       # modify first element
whales[2:5] = [10, 11, 12]  # modify a range of elements
print(whales)

# -----------------------------------------------------------

# 5. Different List Types
list1 = [1, 2, 3, 4]
list2 = [False, True, False]
list3 = ["Hello", "World"]
list_mixed = [1, "Hello", True]
list_nested = [[1, 2, 3, 4], [5, 6, 7, 8]]

print(list_nested[0][1])  # access element in nested list

# -----------------------------------------------------------

# 6. Task 3a_1
a, b, c, d, e = 1, 2, 3, 4, 5
numbers = [a, b, c, d, e]
print(numbers)

new_list = [numbers, numbers]
new_list[0] = "hello"
print(new_list)

# -----------------------------------------------------------

# 7. Operations on Lists
# + combines lists, * repeats them, "in" checks membership
print([1, 2] + [3, 4])   # [1, 2, 3, 4]
print([1, 2] * 3)        # [1, 2, 1, 2, 1, 2]
print(2 in [1, 2, 3])    # True
print([1] in [1, 2, 3])  # False, not sublist

# Note: "+" creates a new list; it does not modify the existing one.

# -----------------------------------------------------------

# 8. List Methods
nums = [4, 2, 7, 1]
nums.append(9)          # adds element at end
nums.extend([10, 11])   # adds multiple elements
nums.insert(1, 99)      # insert at position 1
nums.remove(2)          # remove first occurrence of 2
nums.pop()              # remove and return last element
print(nums.index(7))    # index of first 7
print(nums.count(1))    # count occurrences
nums.reverse()          # reverse in place
nums.sort()             # sort ascending in place
print(nums)

# -----------------------------------------------------------

# 9. sorted() vs .sort()
L = [2, 3, 4, 5, 1]
print(sorted(L))  # returns sorted copy
print(L)          # original unchanged
L.sort()
print(L)          # now changed

# -----------------------------------------------------------

# 10. Built-in Functions that Work on Lists
L = [1, 2, 3, 4, 5]
print(len(L))  # 5
print(sum(L))  # 15
print(min(L))  # 1
print(max(L))  # 5

# -----------------------------------------------------------

# 11. The map() Function
def times2(x):
    return x * 2

L = [1, 2, 3, 4, 5]
print(list(map(times2, L)))  # [2, 4, 6, 8, 10]

# -----------------------------------------------------------

# 12. Task 3a_2 - Write mean function
def mean(L):
    return sum(L) / len(L)

print(mean([1, 2, 3, 4, 5]))

# -----------------------------------------------------------

# 13. Task 3a_3 - remove last item
def remove_last(L):
    L.pop()
    return L

print(remove_last([1, 2, 3]))

# -----------------------------------------------------------

# 14. Task 3a_4 - kingdom slicing
kingdoms = ['Bacteria', 'Protozoa', 'Chromista', 'Plantae', 'Fungi', 'Animalia']
print(kingdoms[0])       # first
print(kingdoms[-1])      # last
print(kingdoms[:3])      # first 3
print(kingdoms[2:5])     # middle slice
print(kingdoms[-2:])     # last two
print(kingdoms[3:3])     # empty list

# -----------------------------------------------------------

# 15. Task 3a_5 - Appointments example
appointments = ['9:00', '10:30', '14:00', '15:00', '15:30']
appointments.append('16:30')   # modifies list
print(appointments)

appointments2 = appointments + ['17:00']  # creates new list
print(appointments2)

# append modifies; + creates new list

# -----------------------------------------------------------

# 16. Task 3a_6 - ids list manipulations
ids = [4353, 2314, 2956, 3382, 9362, 3900]
ids.remove(3382)                  # remove element
print(ids.index(9362))            # get index
ids.insert(5, 4499)               # insert after index 5
ids.extend([5566, 1830])          # extend list
ids.reverse()                     # reverse order
ids.sort()                        # sort ascending
print(ids)

# -----------------------------------------------------------

# 17. Task 3a_7 - sorting and slicing
temps = [25.2, 16.8, 31.4, 23.9, 28, 22.5, 19.6]
temps.sort()
cool_temps = temps[:3]
warm_temps = temps[3:]
temps_in_celsius = cool_temps + warm_temps
print(temps_in_celsius)

# -----------------------------------------------------------

# 18. Task 3a_8 - Nested list access
units = [['km', 'miles', 'league'], ['kg', 'pound', 'stone']]
print(units[0])        # first inner list
print(units[-1])       # last inner list
print(units[0][0])     # 'km'
print(units[1][0])     # 'kg'
print(units[0][1:])    # ['miles', 'league']
print(units[1][0:2])   # ['kg', 'pound']

# -----------------------------------------------------------

# 19. Quick Reference / Exam Hints
# - Indexing starts at 0
# - Negative indices go from end
# - Slicing end is exclusive
# - Lists are mutable
# - .append() modifies list, + creates new one
# - .sort() modifies list, sorted() returns a new sorted copy
# - map(function, list) applies a function to each element
# - Nested lists are accessed using multiple brackets
# - Common errors: IndexError, forgetting brackets, modifying vs copying

# End of Lists Summary

print("\n" + "=" * 60)
print("END OF LISTS EXAMPLES - Happy Learning!")
print("=" * 60)