""" Collections module provide varied data structures , that can be used to store and manage data """
import collections
from collections import Counter



# Counter() : a class inside the collection module 
# To count items inside a set 
fruits = ["banana", "kiwi", "pineapple", "kiwi", "apple", "banana", "kiwi", "banana", "apple"]
c = Counter(fruits)
print(c)
print(c["kiwi"])

people ={"niya":3, "thasni":1 ,"basheer":6}
co = Counter(people)
print(co)
print(co["niya"])
print(list(co.elements()))

"""Counter methods()"""
# .elements() : returns an iterable object containing every single elements seperately
con = Counter(cats=4, dogs=6)
print(con)
# returns the object stored in a container or the id will return
print(list(con.elements()))

# .most_common(x) : returns the 'x' most common elements in the object,   
colors = Counter(red = 5, blue = 3, yellow = 12, green = 4)
print(colors.most_common(2))

# .subtract(_) : Subtracts the count of identical elements from the object and the identical the data we pass
letters = Counter(a = 2, b = 4, c = 6, d = 10)
letters2 =  Counter(["a", "b", "d", "d", "d", "a", "b", "d", "c", "c"])
letters3 =  ["a", "b", "a", "b"]
# subtracts from a list
letters.subtract(letters3)
print(letters)
# subtracting from an object of the same class
letters.subtract(letters2)
print(letters)


# .update(_) : adds up the count of identical elements from the object and the identical the data we pass
l = Counter(a = 2, b = 4, c = 5)
l2 =  Counter(["a", "a", "b", "b", "b", "c", "c", "c", "d", "d"])
l3 =  ["a", "a", "a", "b", "d"]

l.update(l3)
print(l)

l.update(l2)
print(l)

# .clear() : removes all the elements and we get an empty object
obj = Counter(["cat", "cat", "dog", "dog", "dog", "cow"])
print(obj)
obj.clear()
print(obj)

"""operations """
A1 =  Counter(["a", "a", "b", "b", "b", "c", "c", "c", "d", "d"])
A2 =  Counter(["a", "a", "a", "b", "d"])

# addition: adds the sums of elements
print(A1+A2)

# subtraction: subtracts the sum of elements
print(A1-A2)

# Intersection: return the number of element inside the operant which has the minimum sum of the common element, it do not return 0 or less
print(A1&A2)

# Union: return the number of element inside the operant which has the minimum sum of the common element, it do not return 0 or less
print(A1|A2)