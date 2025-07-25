# Strings and Conditional Statements
# Strings is data type that stores a sequence of characters.

# str1 = "this is a string. \t we are creating it in python."

# str2 = 'ApnaCollege'
# str3 = """this is a string"""

# # escape sequence characters: tab, nextline, 
# print(str1)


# str1 = "apna"

# len1 = len(str1)
# print(len1)

# str2 = "college"
# len2 = len(str2)
# print(len2)

# final_str = str1 + " " + str2
# print(final_str)


# Indexing
# str = "apna college"
# # ch = str[2]
# print(str[2])

# we cannot modify the characters in a string like this way.
# str[4] = "@"

# Slicing
# Accessing parts of a string
# str[starting_index, ending_index]

# print(str[5 : len(str)])
# print(str[5 : ])  # [5:len(str)]
# print(str[ : 4])  # [0:4]

# Negative index
# str = "apple"
# print(str[-5 : -2])


# String Functions

# endsWith()

str = "i am from studying python from apna college"

# print(str.endswith("ege"))
# print(str.capitalize())  #first character capital no changes inside original string

# # in order to make changes into original string
# str = str.capitalize()
# print(str)


# replace()
# print(str.replace("python", "javascript"))

# # find()
# print(str.find("from"))

# # count()
# print(str.count("o"))

# # Write a program to input user's first name & print its length
# firstName = input("Enter first Name: ")
# print(len(firstName))

# # Write a program to find the occurance of "$" in a string
# str = "Hi, $Iam the $ symbol $99.99"
# print(str.count("$"))


# Conditional Statements
#  if-elif-else (SYNTAX)

# age = 21

# if(age >= 18):
#     print("can vote")
#     print("can drive")

# light = "yellow"

# if(light == "red"):
#     print("stop!")
# elif(light == "green"):
#     print("go!") 
# elif(light == "yellow"):
#     print("look!")
# else:
#     print("light is broken")    
    
# print("end of code")

# num = 5

# if(num > 2):
#     print("greater than 2")
# elif(num > 3):
#     print("greater than 3")


# age = 14

# if(age >= 18):
#     print("can vote")   # indentation
# else:
#     print("cannot vote")


# marks = int(input("Enter Student Marks: "))

# if(marks >= 90):
#     grade = "A"
# elif(marks >= 80 and marks < 90):
#     grade = "B"
# elif(marks >= 70 and marks <80):
#     grade = "C"
# else:
#     grade = "D"
    
# print("grade of the student => ", grade)


# nesting - if statements

# age = 34

# if(age >= 18):
#     if(age >= 80): 
#         print("cannot drive")
#     print("can drive")
# else: 
#     print("cannot drive")


# Write a program to check if a number entered by the user is odd or even

# num = int(input("Enter the Number: "))

# if(num % 2 == 0):
#     print("EVEN")
# else: 
#     print("ODD")
    

# # Write a program to find the greatest of 3 numbers entered by the user.
# num1 = int(input("Enter num1: "))
# num2 = int(input("Enter num2: "))
# num3 = int(input("Enter num3: "))
    
# if(num1 >= num2 and num1 >= num3):
#     print(num1, " is greatest")
# elif(num2 >= num3):
#     print(num2, " is greatest")
# else: 
#     print(num3, " is greatest")
    
    
# Write a program to check if a number is a multiple of 7 or not
# num = int(input("Enter the number: "))

# if(num % 7 == 0):
#     print(num, " is a multiple of 7")
# else:
#     print(num, " is not the multiple of 7")


# Write a program to find the greatest amoung four numbers
num1 = int(input("Enter num1: "))
num2 = int(input("Enter num2: "))
num3 = int(input("Enter num3: "))
num4 = int(input("Enter num4: "))

if(num1 >= num2 and num1 >= num3 and num1 >= num4):
    print(num1, " is largest")
elif(num2 >= num3 and num2 >= num4):
    print(num2, " is largest")
elif(num3 >= num4): 
    print(num3, " is largest")
else:
    print(num4, " is largest")
    
    
    
