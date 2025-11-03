# Note:
#   to run each sample you may remove the docstring (''') wrap around the code sample you want to run. Thanks :)

'''
    Data Containers -> A data container is simply a structure that can hold multiple pieces of data (values, objects, or even other containers).
                    -> Think of it like a box where you store and organize data.
                    -> Different containers have different rules (ordered/unordered, mutable/immutable, allow duplicates or not).
'''

# ----------------------------------- TUPPLES -----------------------------------
'''
    tuple -> A tuple is an ordered, immutable sequence type in Python.
          -> Syntax: t = (1, 2, 3) or t = 1, 2, 3.
          -> Singleton tuple needs a trailing comma: (42,).
          -> Tuples are hashable if and only if every element inside is hashable — so tuples can be used as dict keys or set elements when contents are hashable.
'''
# tupple examples

# --- Example 1 ---
'''
#           0  1  2    3      4
a_tupple = (1, 2, 3, "word", 4.5)
print(a_tupple[2])
'''
# --- Example 2 ---

# 1. Calculate average for each student
# 2. Find top student
# 3. Add score 100 to Bob
# 4. Remove lowest score from Alice

# Initial data

students = (
    ('Alice', (90, 85, 92)),
    ('Bob', (78, 81)),
    ('Charlie', (88, 90, 95, 93))
    )

# Answers
# 1.)
'''
for student in students:
    name = student[0]
    scores = student[1]
    average = sum(scores) / len(scores)
    print(name, f"{average:.2f}")
'''
# 2.)
'''
# Initialize variables to track top student
top_student = None
highest_avg = 0 # first iteration 89.00

for name, scores in students:
    avg = sum(scores) / len(scores)
    if avg > highest_avg:
        highest_avg = avg
        top_student = name

print(f"Top student: {top_student} with average {highest_avg}")
'''
# 3.)
'''
students = (
    ('Alice', (90, 85, 92)),
    ('Bob', (78, 81, 100)),
    ('Charlie', (88, 90, 95, 93))
    )

print(students)
'''
# 4.)
'''
students = students = (
    ('Alice', (90, 92)),
    ('Bob', (78, 81, 74, 100)),
    ('Charlie', (88, 90, 95))
)

print(students)
'''

# ----------------------------------- LISTS -----------------------------------
'''
    Lists -> A list is an ordered collection of items.
          -> Unlike tuples, lists are mutable, meaning you can add, remove, or change elements.
          -> Lists are defined with square brackets [].

    Why lists are useful compared to tuples?
        -> You can change data dynamically (tuples can’t).
        -> Ideal for things like:
            -> Storing user inputs that change
            -> Keeping track of scores, tasks, or inventory
            -> Iterating and modifying elements
'''
# lists examples

# --- Example 1 ---
'''
#            0         1         2
fruits = ['apple', 'banana', 'cherry']

# 2. Key operations on lists

# Operation	        Example	                    Output / Effect
# --------------------------------------------------------------
# Access	        fruits[0]	                'apple'
# Update	        fruits[1] = 'orange'	    ['apple', 'orange', 'cherry']
# Append	        fruits.append('mango')	    Adds at the end
# Insert	        fruits.insert(1, 'kiwi')	Insert at index 1
# Remove by value	fruits.remove('cherry')	    Removes 'cherry'
# Remove by index	fruits.pop(0)	            Removes 'apple'
# Length	        len(fruits)	                4
# Slice	            fruits[1:3]	                ['kiwi', 'orange']

fruits[1] = 'orange'
fruits.append('mango')	
fruits.insert(1, 'kiwi')
fruits.remove('cherry')
fruits.pop(0)

print(fruits[1:3])
'''
# --- Example 2 ---
'''
#               0          1
students = [['Alice', [90, 85, 92]],
            ['Bob', [78, 81, 74]],
            ['Charlie', [88, 90, 95]]
            ]

# Add a new student
students.append(['David', [80, 85, 88]])

# Update a score
students[0][1].append(100)  # Add a new score to Alice

# Print all students

for student in students:
    name = student[0]
    grades = student[1]
    average = sum(grades) / len(grades)
    print(name, grades, f"{average:.2f}")
'''
# ----------------------------------- SETS -----------------------------------
'''
    Sets -> An unordered collection (no specific order).
         -> A mutable data structure (you can add/remove items).
         -> Does not allow duplicates.
         -> You define it with curly braces {} or the set() function.
'''
# Sets Examples

# --- Example 1 ---
'''
# Creating a set
fruits = {"apple", "banana", "cherry"}
print(fruits)

fruits.add("orange")      # add one item
fruits.update(["mango"])  # add multiple items
fruits.remove("banana")   # remove (error if not found)
fruits.discard("grape")   # remove (no error if not found)
print(fruits)
'''
# --- Example 2 ---
'''
# Duplicates are removed automatically
nums = {1, 2, 2, 3, 4, 4}
print(nums)  # {1, 2, 3, 4}
'''

# == The 4 Basic Set Operations ==

# data sample for the 4 basic set operations

a = {1, 2, 3, 4}
b = {3, 4, 5, 6}

# 1.) Union (| or .union()) -> Takes all unique elements from both sets.
'''
# --- Union Example ---

print(a | b)             # {1, 2, 3, 4, 5, 6}
print(a.union(b))        # same result
'''

# 2.) Intersection (& or .intersection()) -> Takes elements common to both sets.

# --- Intersection Example ---
'''
print(a & b)             # {3, 4}
print(a.intersection(b)) # same result
'''

# 3.) Difference (- or .difference()) -> Takes elements in one set but not in the other.

# --- Difference Example ---
'''
print(a - b)             # {1, 2} (in a but not in b)
print(b - a)             # {5, 6} (in b but not in a)
'''

# 4.) Symmetric Difference (^ or .symmetric_difference())
'''
print(a ^ b)                     # {1, 2, 5, 6}
print(a.symmetric_difference(b)) # same result

'''

# --- Example 3 ---
# 1. Calculate average for each student
# 2. Find top student
# 3. Add score 100 to Bob
# 4. Remove lowest score from Alice
'''
students = {
    "Alice": {90, 85, 92},
    "Bob": {78, 81, 74},
    "Charlie": {88, 90, 95}
} 
'''
# 1.)
'''
for name, scores in students.items():
    avg = sum(scores) / len(scores)
    print(name, avg)
'''

# 2.)
'''
top_student = None
highest_avg = 0  # start with 0 so any real avg will be higher

for name, scores in students.items():
    avg = sum(scores) / len(scores)
    if avg > highest_avg:
        highest_avg = avg
        top_student = name

print("Top student:", top_student, "with average", highest_avg)
'''

# 3.)
'''
students["Bob"].add(100)
print("Bob’s scores:", students["Bob"])
'''

# 4.) 
'''
students["Alice"].remove(min(students["Alice"]))
print("Alice’s scores:", students["Alice"])
'''

# ----------------------------------- DICTIONARIES -----------------------------------
'''
    Dictionaries -> A dictionary in Python is a collection of key–value pairs.
                 -> Keys are unique (like an index, but you choose what they are).
                 -> Values can be anything (numbers, strings, lists, sets, other dicts…).
                 -> Defined with {} using the form {key: value}.
'''
# Dictionary examples

# Example 1

student = {
    "name": "Alice",
    "age": 20,
    "scores": [90, 85, 92]
}
'''
print(student["name"])   # Alice
print(student["scores"]) # [90, 85, 92]
'''

# == Common Dictionary Operations ==

# --- Accessing & Updating ---
'''
print(student["age"])      # 20
student["age"] = 21        # update value
student["major"] = "CS"    # add new key-value pair
print(student)
'''

# --- Removing ---
'''
student.pop("age")     # remove by key
del student["scores"]  # remove by key
student.clear()        # remove all
'''

# --- Looping ---
'''
for key in student:
    print(key, student[key])    # key + value

for key, value in student.items():
    print(key, value)           # same, but unpacked
'''

# --- Useful Methods ---
'''
print(student.keys())    # all keys

print(student.values())  # all values
print(student.items())   # all key-value pairs
'''

# --- Example 2 ---
# 1. Calculate average for each student 
# 2. Find top student 
# 3. Add score 100 to Bob 
# 4. Remove lowest score from Alice

'''
students = {
    "Alice": {"Math": 90, "Science": 85, "English": 92},
    "Bob": {"Math": 78, "Science": 81, "English": 74},
    "Charlie": {"Math": 88, "Science": 90, "English": 95}
}
'''

# 1.)
'''
for name, subjects in students.items():
    avg = sum(subjects.values()) / len(subjects)
    print(name, "average:", avg)

'''

# 2.)
'''
top_student = None
highest_avg = 0

for name, subjects in students.items():
    avg = sum(subjects.values()) / len(subjects)
    if avg > highest_avg:
        highest_avg = avg
        top_student = name

print("Top student:", top_student, "with average", highest_avg)
'''

# 3.)
'''
students["Bob"]["History"] = 100
print("Bob’s scores:", students["Bob"])
'''

# 4.)
'''
lowest_subject = min(students["Alice"], key=students["Alice"].get)
students["Alice"].pop(lowest_subject)
print("Alice’s scores:", students["Alice"])
'''