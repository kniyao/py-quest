""" Collections module provide varied data structures , that can be used to store and manage data """
import collections
from collections import Counter



# Counter() : a class inside the collection module 
# To count objects inside containers or charecters inside strings
fruits = ["banana", "kiwi", "pineapple", "kiwi", "apple", "banana", "kiwi", "banana", "apple"]
c = Counter(fruits)
print(c)
print(c["kiwi"])

people ={"niya":3, "thasni":1 ,"basheer":6}
co = Counter(people)
print(co)
print(co["niya"])
print(list(co.elements()))

con = Counter(cats=4, dogs=6)
print(con)
print(list(con.elements()))



