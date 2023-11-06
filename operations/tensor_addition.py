# Vector Addition

# Task 1
# Create a function that takes two vectors as arguments
# The function should add the values of the vector, and return the result as a vector
# Eg: [1, 2] + [3, 4] = [4, 6]

def adding_vectors(vec1,vec2):
    if len(vec1) == len(vec2):
        result = []
        for x in range(len(vec1)):
            result.append(vec1[x] + vec2[x])
        return result
    else:
        return "sorry, The length of the lists should be same!"

print(adding_vectors([1,2,3],[1,2,3]))

