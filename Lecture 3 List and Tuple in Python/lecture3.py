# list and Tuples in Python

# list in Python

# marks1 = 94.4
# marks2 = 87.5
# marks3 = 95.4
# marks4 = 66.3
# marks5 = 45.4


# marks = [94.4, 87.5, 95.2, 66.4, 45.1]
# print(marks)
# print(type(marks))
# print(len(marks))
# print(marks[0])
# print(marks[1])

# student = ["krishna", 99.4, 17, "Delhi"]

# student[0] = "Arjun"
# print(student)

# strings are immutable in python
# lists are mutable in python

# str = "hello"
# print(str[0])
# str[0] = "y"

# list slicing similar to String slicing
# list_name[starting_index : ending_index] ending index is not included

# marks = [85, 94, 76, 63, 48]
# print(marks[1 : 4])
# print(marks[1 : ])
# print(marks[ : 4])

# list methods
# list = [2, 1, 3]

# # append() adds one element to the end
# list.append(4)
# # print(list.append(4))
# print(list)

# # sort method - sorts in ascending order
# list.sort()
# # print(list.sort())
# print(list)

# # sorting in descending order
# list.sort(reverse = True)
# print(list)

# list = ["banana", "litchi", "apple"]

# print(list.sort(reverse=True))

# list.sort()
# print(list)

# # reverse list - reverses list [3, 2, 1]
# list = ['a', 'd', 'e', 'f', 'c', 'b']
# list.reverse()
# print(list)

# insert Method = inserts element at index
# list = [2, 1, 3]
# list.insert(1, 5)
# print(list)

# remove() method - remove the first occurance of element
# list = [2, 1, 3, 1]
# list.remove(1)
# print(list)

# pop() - removes element at index
# list.pop(2)
# print(list)

# Review python documentation for methods in Array

# Tuples in Python
# A built-in data type that lets us create immutable sequence of values
# strings, tuple => Immutable
# list => mutable

# tup = (2, 1, 3, 1)
# print(type(tup))
# print(tup[0])
# print(tup[1])

# # we cant change the value by going to certain index in case of tuples
# tup[0] = 5

# empty tuple
# tup = ()
# print(tup)
# print(type(tup))

# if we have a single element in a tuple we seperate it with comma
# tup = (1, )
# print(tup)
# print(type(tup))


# Slicing in Tuples
# tup = (1, 2, 3, 4, 2, 2)
# print(tup[1 : 3])

# # tup.index(el) returns index of first occurance
# print(tup.index(2)) # returns the index

# # tup.count(el) counts total occurances of the element
# print(tup.count(2))



# Practice Questions
# Write a program to ask user to enter names of their 3 favourite movies and store them in a list.
# movies = []

# movie1 = input("Enter first movie: ")
# movie2 = input("Enter second movie: ")
# movie3 = input("Enter third movie: ")

# movies.append(movie1)
# movies.append(movie2)
# movies.append(movie3)
# print(movies)

# Write a program to check if a list contains a palindrome of elements. (hint use copy() method)
# list1 = [1, 2, 1]
# list2 = [1, 2, 3]

# list1 = ["m", "a", "a", "m"]

# copy_list1 = list1.copy()
# copy_list1.reverse()

# if(copy_list1 == list1): 
#     print("Palindrome")
# else:
#     print("Not Palindrome")
    
    
    
# copy_list2 = list2.copy()
# copy_list2.reverse()

# if(copy_list2 == list2):
#     print("Palindrome")
# else:
#     print("Not Palindrome")


# Write a program to count the number of students with the "A" grade in the following tuple: 
grade = ("C", "D", "A", "A", "B", "B", "A")
print(grade.count("A"))


# store the above values in a list & sort them from "A" to "D" -> ascending order
grade = ["C", "D", "A", "A", "B", "B", "A"]
grade.sort()
print(grade)

