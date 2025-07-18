# print("Hare Krishna!");
# print("Krishna", "My age is 25");
# print(23);
# print(35 + 23);

# Variables in Python
name = "Krishna";   #string
age = 23;           # using assignment operator
price = 25.99;

# print("My name is: ", name);
# print("My Age is: ", age);
# print(price);

age2 = age;
# print("Age2: ", age2);
# print(type(name))
# print(type(age))
# print(type(price))


# Data Types in Python
# Integers        +ve, -ve, 0
# String           "krishna"
# Float          3.99  2.5  9.0
# Boolean         True, False
# None            a = None;


# name1 = "sk";
# name2 = "sk";
# name3 = '''sk''';

# print(name1);
# print(name2);
# print(name3);

age = 23;
old = False;
a = None;

# print(type(age));            #  <class 'int'>
# print(type(old));            #  <class 'bool'>
# print(type(a));              # <class 'NoneType'>


# Keywords in python:
# Python is case sensitive

# Print Sum of Two Numbers:
# a = 2;
# b = 5;

# print(a + b);
# print(a - b);
# print("hello world");


# Comments in Python
#print("hello world");

""" 
multi-line comment 

"""

# Operators in Python

""" 
Types of Operators:
Arithmetic operators
Relational/Comparison Operators
Assignment Operators
Logical Operators

"""


# arithmetixc operators
# a = 5
# b = 2

# print(a + b)
# print(a - b)
# print(a * b)
# print(a / b)
# print(a % b)   # remainder
# print(a ** b)  # a ^ b

# Relational Operators
a = 50
b = 20

# print(a == b)  # False
# print(a != b)
# print(a >= b)
# print(a > b)
# print(a <= b)
# print(a < b)


# Assingment Operator
# num = 10
# num += 10
# num -= 10
# num *= 10
# num /= 10
# num **= 5
# print("num: ", num)


# logical Operators  (not, and, or)
a = 50
b = 30
# print(not False)
# print(not (a > b))


val1 = True
val2 = False

# print("AND operator: ", val1 and val2)
# print("OR operator: ", val1 or val2)
# print("OR operator: ", val1 or val2) 
# print("Comparison: a, b: ", (a == b) or (a > b))


# Type Conversion
# type conversion => automatically
# type casting => manually explicit type conversion


# Type Conversion
# a = 2
# b = 4.25

# sum = a + b   #  2.0 + 4.25

# print(sum)


# a = "2"
# b = 4.25

# sum = a + b   #  2.0 + 4.25

# print(type(a))

# Type Casting
# a = float("2")
# b = 4.25

# sum = a + b   #  2.0 + 4.25

# print(type(a))
# print(sum)


# a = 3.14
# a = str(a)

# print(type(a))


# Input in Python
# input() statement is used to accept values from the user.

# name = input("Enter your name: ")
# print("Welcome: ", name)

# age = input("Enter your age: ")
# print("You entered: ", age)


# val = input("enter some value: ")
# print(type(val), val)   # "25"  "99.99" "apnacollege"

# Type Casting
# val = int(input("Enter some value: "))
# print(type(val), val)


# val = float(input("Enter some value: "))
# print(type(val), val)

# name = input("enter name: ")
# age = int(input("enter age: "))
# marks = float(input("enter marks: "))

# print("welcome", name)
# print("age: ", age)
# print("marks: ", marks)

# Practice Questions
# Write a Program to input 2 numbers and print their sum

# first = int(input("Enter first number: "))
# second = int(input("Enter second number: "))
# sum = first + second
# print("sum = ", sum)

# Write a program to input side of a square & print its area

# side = float(input("enter the square side: "))
# print("area of square: ", side ** 2)

# write a program to input 2 floating point numbers & print their average
# a = float(input("Enter first number: "))
# b = float(input("Enter second number: "))

# print("avg: ", (a + b)/2)


#  Write a program to input 2 int numbers, a and b
# Print True if a is greater than or equal to b. If not print False

a = int(input("Enter value for number a: "))
b = int(input("Enter value for number b: "))

# if(a >= b) :
#     print(True)
# else :
#     print(False)


print(a >= b)