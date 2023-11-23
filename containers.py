""" 
    --> Containers enables us to organize, store, and manage collections of data.
    --> Types of containers: List, Tuple, Dictionaries, Sets
 """
# List: Ordered collection of data that is mutable, represented by []
p1 = ["Niya", 12]
print(p1)
p1[1] = 13
print(p1)
 
# Tuples: Ordered collection of data but are immutable, represented by ()
p2 = ("niya", 13)
print(p2,)
# p2[1] = 14
# print(p2)

# Dictionaries: collection of keyvalue pairs that is unordered, represented by {}
Book = {"name":"Sherlock holmes : The hount of baskerville", "author":"Arthur Conan Doyle", "year":"1926" }
print(Book)
print(Book["name"])

# Sets: collection of unique elements that is unordered
# creating sets using the built in function
p3 = ["Basheer", 27, "tall", "hungry"]
set(p3)

# creating sets using curly braces
p4 = {"thasni", 19, "short", "wierd"}
print(p4)