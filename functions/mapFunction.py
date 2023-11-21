# example 1
lis = [1,2,3,4,5,6,7,8,9,10]
# returns if the num is even or not
def func(x):
    return x % 2 == 0

"""    
    --> Map function takes a function and an iterable as arguments 
    --> Applies the function on every element of the iterable
    --> returns the value of each execution
    --> It needs to return a list as output 
    """
map1 = list(map(func,lis))
print(map1)

# example 2
text = "Hello World!"
# returns the input text to all upper case
def up(txt):
    return txt.upper()

test1 = list(map(up,text))
print(test1)



#LIST COMPREHENSATION
"""
    --> Returns a list based on the values of an existing iterable
    --> We add a function/another comprehensationlist/ a simple expression as an expression 
    --> give a placeholder for the item(iterable) 
    --> We can add condition to the comprehensation
    --> [*expression* for *item* in *iterable* if *condition*]
        """
# example 1
li = [1,2,3,4,5,6,7,8,9,10]

def fun(x):
    return x ** 2

list1 = [fun(x) for x in li if x < 5]
print(list1)

# example 2
te = "Hello World!"

def upp(tx):
    return tx.upper()


list2 = [upp(tx) for tx in te]
print(list2)