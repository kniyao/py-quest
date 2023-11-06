# Task 2
# Create a class - Tensor that would create vectors
# The objects should be able to be operated upon with numerical operators, such as +, -, *, /.

class Vector:
    def __init__(self, vector):
        self.vector = vector

    def add(self, vector_to_add):
        addingVec = len(vector_to_add.vector)
        if len(self.vector) == addingVec:
            val = []
            for i in range(addingVec):
                val.append(self.vector[i] + vector_to_add.vector[i])
            return Vector(val)
        else:
            return "Error"
    
    def subtract(self, vector_to_subtract):
        subtractingVec = len(vector_to_subtract.vector)
        if len(self.vector) == subtractingVec:
            val = []
            for i in range(subtractingVec):
                val.append(self.vector[i] - vector_to_subtract.vector[i])
            return Vector(val)
        else:
            return "Error"
    
    def multiply(self, vector_to_multiply):
        multiplyingVec = len(vector_to_multiply.vector)
        if len(self.vector) == multiplyingVec:
            val = []
            for i in range(multiplyingVec):
                val.append(self.vector[i] * vector_to_multiply.vector[i])
            return Vector(val)
        else:
            return "Error"
        
    def divide(self, vector_to_divide):
        dividingVec = len(vector_to_divide.vector)
        if len(self.vector) == len(vector_to_divide.vector):
            val = []
            for i in range(dividingVec):
                val.append(self.vector[i] / vector_to_divide.vector[i])
            return Vector(val)
        else:
            return "Error!"
    


        
        


v1 = Vector([7,4])
v2 = Vector([1,3])

v3 = v1.divide(v2)
print(v3.vector)
