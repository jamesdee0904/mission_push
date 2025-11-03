'''
# Variables

# Example: Storing and printing student information

# A variable is like a container that holds data
student_name = "Alex"       # String variable (text)
student_age = 18            # Integer variable (number without decimal)
student_gpa = 3.5           # Float variable (number with decimal)

# Printing the values stored in variables
print("Name:", student_name)
print("Age:", student_age)
print("GPA:", student_gpa)
'''

'''
# If-Else Condition

# Example: Checking if a student passed the exam

score = 75   # Store the exam score in a variable

# If-else is used to make decisions
if score >= 60:
    # This block runs if the condition is TRUE
    print("Congratulations! You passed the exam.")
else:
    # This block runs if the condition is FALSE
    print("Sorry, you did not pass. Please try again.")
'''

'''
# Arithmetic Operators

# Example: Simple calculator for two numbers

a = 10
b = 3

# Arithmetic operators: +, -, *, /, %, //
print("Addition:", a + b)        # 10 + 3 = 13
print("Subtraction:", a - b)     # 10 - 3 = 7
print("Multiplication:", a * b)  # 10 * 3 = 30
print("Division:", a / b)        # 10 / 3 = 3.333...
print("Modulus:", a % b)         # 10 % 3 = 1 (remainder)
print("Floor Division:", a // b) # 10 // 3 = 3 (quotient only)
'''

'''
# Comparison and logical operators

# Example: Checking if a person can vote

age = 20
citizen = True   # Boolean value (True/False)

# Comparison: ==, !=, >, <, >=, <=
# Logical: and, or, not

if age >= 18 and citizen == True:
    print("You are eligible to vote.")
else:
    print("You are NOT eligible to vote.")
'''

'''
# Loops -> For loops

# Example: Printing numbers from 1 to 5

# For loop repeats a block of code a fixed number of times
for i in range(1, 6):    # range(1, 6) means 1 to 5
    print("Number:", i)
'''

'''
# Loops -> while loops

# Example: Countdown timer

count = 5

# While loop runs as long as the condition is TRUE
while count > 0:
    print("Countdown:", count)
    count -= 1   # Decrease count by 1 each time

print("Blast off!")
'''

# Encapulation -> Getter and Setter

# Example: Bank Account with encapsulation

"""class BankAccount:
    def __init__(self, account_number, balance):
        self.account_number = account_number   # public variable
        self.__balance = balance               # private variable (note the __)

    # Getter method → to access private variable
    def get_balance(self):
        return self.__balance

    # Setter method → to safely update private variable
    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount
            print(f"Deposited {amount}. New balance: {self.__balance}")
        else:
            print("Invalid deposit amount.")

    def withdraw(self, amount):
        if 0 < amount <= self.__balance:
            self.__balance -= amount
            print(f"Withdrew {amount}. New balance: {self.__balance}")
        else:
            print("Insufficient balance or invalid amount.")

# Create object
account = BankAccount("12345", 1000)

# Access balance safely
print("Balance:", account.get_balance())

# Update balance safely
account.deposit(500)
account.withdraw(200)

# Try to access private variable directly (not recommended!)
#print(account.__balance)   # This would cause an error
"""

"""
# Inheritance

# Inheritance means: "Child class can use the properties and methods of a Parent class."

# Parent class → Shape
class Shape:
    def __init__(self, name):
        self.name = name
    
    def describe(self):
        return f"This is a {self.name}."

# Child class → Rectangle (inherits from Shape)
class Rectangle(Shape):
    def __init__(self, width, height):
        # Call the parent constructor using super()
        super().__init__("Rectangle")
        self.width = width
        self.height = height
    
    def area(self):
        return self.width * self.height

# Another child class → Circle (inherits from Shape)
class Circle(Shape):
    def __init__(self, radius):
        super().__init__("Circle")
        self.radius = radius
    
    def area(self):
        return 3.14 * (self.radius ** 2)

# Create objects
rect = Rectangle(4, 5)
circle = Circle(3)

# Both child classes can use 'describe()' from the parent class
print(rect.describe())       # "This is a Rectangle."
print("Rectangle area:", rect.area())   # 20

print(circle.describe())     # "This is a Circle."
print("Circle area:", circle.area())    # 28.26
"""

"""
# Polymorphism

# Example: Different shapes with same "area" method

# Polymorphism with math example:
# Different shapes have the SAME method name "area"
# but they calculate it in DIFFERENT ways.

class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height
    
    def area(self):
        # Formula: width × height
        return self.width * self.height

class Circle:
    def __init__(self, radius):
        self.radius = radius
    
    def area(self):
        # Formula: π × r²
        return 3.14 * (self.radius ** 2)

class Triangle:
    def __init__(self, base, height):
        self.base = base
        self.height = height
    
    def area(self):
        # Formula: 1/2 × base × height
        return 0.5 * self.base * self.height

# Create objects from each class
rect = Rectangle(4, 5)
circle = Circle(3)
tri = Triangle(6, 4)

# Each object calls the SAME method name 'area',
# but produces DIFFERENT results depending on the class
print("Rectangle area:", rect.area())   # 20
print("Circle area:", circle.area())    # 28.26
print("Triangle area:", tri.area())     # 12.0

"""
