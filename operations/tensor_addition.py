# Vector Addition

# Task 1
# Create a function that takes two vectors as arguments
# The function should add the values of the vector, and return the result as a vector
# Eg: [1, 2] + [3, 4] = [4, 6]


# Task 2
# Create a class - Tensor that would create vectors
# The objects should be able to be operated upon with numerical operators, such as +, -, *, /.

def adding_vectors(vec1,vec2):
    if len(vec1) == len(vec2):
       for x in range(len(vec1)):
           result = []
           result = vec1[x] + vec2[x]
           print(result)
    else:
        print("sorry, The length of the lists should be same!")

adding_vectors([1,3,2],[5,4,3])