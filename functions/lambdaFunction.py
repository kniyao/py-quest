"""
    --> used to write functions that only have one expression to return
    --> it takes up little much space
    --> takes arguments and can only return one expression
    """
# we gave lambda function 'x' as a parameter 
# it returns the value of x**2.
# Lastly, we stored the lambda function in a variable

funct = lambda x: x**2

print(funct(3))
print(funct(8))

# lambda inside another function
def cubeOf(x):
    func = lambda y: y ** 3
    return func(x)

print (cubeOf(3))
print (cubeOf(5))

# lambda with multiple parameters and optional parameter
multi = lambda y,z=1: y * z

print(multi(5,4))
print(multi(8))


""" USE THE LAMBDA WITH OTHER BUILT IN FUNCTIONS """
li = [1,2,3,4,5,6,7,8,9,10]
# Lambda with map()
double = list(map(lambda x: x*2, li))

print(double)

# Lambda with filter()
oddOne = list(filter(lambda y: y%2 != 0,li))
print(oddOne)