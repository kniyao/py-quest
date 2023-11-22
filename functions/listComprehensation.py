
#LIST COMPREHENSATION
"""
    --> It allows to filter, map, and transform elements of an iterable into a new list in a single expression
    --> Returns a list based on the values of an existing iterable
    --> We add a function/another comprehensationlist/ a simple expression as an expression 
    --> give a placeholder for the current item 
    --> We can add condition to the comprehensation which decidec to whether include the item in the output or not
    --> [*expression* for *item* in *iterable* if *condition*]
        """
# example 1
li = [1,2,3,4,5,6,7,8,9,10]

def fun(x):
    return x ** 2

# applying the fun() to every item inside the li(like map()) and also checks the condition and only returns those items with True value(like filter())
list1 = [fun(x) for x in li if x < 5]
print(list1)

# example 2
te = "Hello World!"

def upp(tx):
    return tx.upper()

# list comprehensation without the condition
list2 = [upp(tx) for tx in te]
print(list2)