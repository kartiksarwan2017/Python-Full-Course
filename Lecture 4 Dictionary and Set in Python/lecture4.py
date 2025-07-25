# Dictionary and Sets in Python
# Dictionaries are used to store data values in key:value pairs.
# They are unordered, mutable(changeable) & dont allow duplicate keys.

# key could be string, integer, floating value, tuple
info = {
    "name": "Krishna",
    "subjects": ["Python", "C", "Java"],
    "topics": ("dict", "set"),
    "learning": "coding",
    "age": 14,
    "isAdult": True,
    "marks": 94.4
}


# null_dict = {}
# print(null_dict)

# null_dict["name"] = "Hare krishna"
# print(null_dict)

# print(info)
# print(type(info))
# print(info["name"])
# print(info["subjects"])

# info["name"] = "hare Krishna"    #overwrite
# info["surname"] = "krishna"
# print(info["surname"])
# print(info["name"])


# Nested Dictionaries
# student = {
#     "name": "rahul kumar",
#     "subjects": {
#         "phy": 97,
#         "chem": 89,
#         "maths": 96
#     }
# }

# print(student["subjects"]["chem"])

# Dictionary Methods
# keys() retuns all keys

# print(student.keys())
# print(list(student.keys()))
# print(len(student))  # total no. of key values pairs
# print(len(list(student.keys()))) 

# values() - returns all values
# print(student.values())
# print(list(student.values()))

# items() Method - returns all (key, value) pairs as tuples
# print(student.items())
# print(list(student.items()))

# pairs = list(student.items())
# print(pairs[1])

# get() Method => returns the key according to value
# print(student["name2"]) # error
# print(student.get("name2"))   # no error => None as output

# update() Method = inserts the specified items to the dictionary
# new_dict = {"name": "neha kumari", "city": "delhi", "age": 16}
# student.update(new_dict)
# print(student)


# Sets in Python
# Set is the collection of the unordered items.
# Each element in the set must be unique & immutable
# we can store boolean, int, float, str, tuple values into the set
# we cannot store list and dictionary in python => they are mutable

# collection = {1, 2, 2, 2, 3, 4, "hello", "world", "world"}

# print(collection)
# print(type(collection))
# print(len(collection))  # total number of items

# collection = {}  # empty dictionary
# print(type(collection))

# collection = set() # empty set
# print(type(collection))

# set methods
# set.add() Method adds and element
# set.remove(el) removes the element el
# set.clear() empties the set
# set.pop()  removes a random value

# set => immutable 
# set elements -> immutable

# collection = set()
# collection.add(1)
# collection.add(2)
# collection.add(2)


# collection.remove(1)
# collection.remove(7)

# collection.add("hare krishna")
# collection.add((1, 2, 3))

# collection.add([1, 2, 3])
# print(collection)


# immutable => hash value
# hashable values => not changeable

# unhashable => diff value => dict, set, list

# collection.clear()
# print(len(collection))


# collection = {"hello", "apnacollege", "World", "coding", "python"}

# print(collection.pop())
# print(collection.pop())


# set1.union(set2) combines both set values & returns new
# set1 = {1, 2, 3}
# set2 = {2, 3, 4}

# print(set1.union(set2))
# print(set1)
# print(set2)

# set1.intersection(set2)  combines common values & returns new
# print(set1.intersection(set2))
# print(set1)
# print(set2)

# the union and intersection methods does not change the original set it creates a new set


# Practice Questions
# store following word meanings in a python dictionary:
# table: "a piece of furniture", "list of facts & figures"
# cat: "a small animal"

# dictionary = {
#     "table": ["a piece of furniture", "list of facts & figures"],
#     "cat": "a small animal"
# }

# print(dictionary)

# # you are given a list of subjects for students. Assume one classroom is required for 1 subject. Hoe many classrooms are needed
# # by all students
# # "python", "java", "C++", "python", "javascript"
# # "java", "python", "java", "C++", "C"

# subjects = {"python", "java", "c++", "python", "javascript", "java", "python", "java", "C++", "C"}
# print(subjects)
# print(len(subjects))

#  Write a program to enter marks of 3 subjects from the user and store them in a dictionary. Start with an empty
#  dictionary & add one by one. Use subject name as key & makrs as value.

# marks = {}

# phyMarks = int(input("enter phy: "))
# marks.update({"phy": phyMarks})

# chemMarks = int(input("Enter chem: "))
# marks.update({"chem": chemMarks})

# mathsMarks = int(input("Enter maths: "))
# marks.update({"maths": mathsMarks})

# print(marks)


# Figure out a way to store 9 & 9.0 as seperate values in the set.
# you can take hlep of built-in data types

# values = {9, "9.0", 9.25, 8, 8.0}
# print(values)


values = {
    ("float", 9.0), 
    ("int", 9)
}

print(values)