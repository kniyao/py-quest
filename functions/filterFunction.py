li = [1,2,3,4,5,6,7,8,9,10]

def isEven(x):
    return x % 2 == 0


"""    
    --> Filter function takes a function and an iterable as arguments 
    --> Applies the function on every element of the iterable
    --> Return only the items that has the TRUE outcome when executing the function (like a filter)
    --> It needs to return a list as output 
    """

list1 = list(filter(isEven,li))
print(list1)

"""    
    --> Filter function can be combined with the Map function
    --> apply map() on every item that the filter() returned/ vice versa
    """
def square(y):
    return y ** 2

list2 = list(map(square,filter(isEven,li)))
print(list2)
