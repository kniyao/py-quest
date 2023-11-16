class Person:
    # class variable
    count = []

    def __init__(self, name, age):
        self.name = name
        self.age = age
        self.count.append(self.name)
    
    # below a classmethod is given , it can be used to do operations on the class itself
    # cls : refers to the class
    @classmethod 
    def countObjects(cls):
        return len(cls.count)
    # below a classmethod is given , it usually have nothing to do with the instance or the class, except that it is stored inside the class 
    @staticmethod
    def greet(i):
        for loop in range(i):
            print("hello")
    
    

    


p1 = Person("niya", 13)
p2 = Person("thasni", 19)
p3 = Person("rinu", 11)
p4 = Person("anu", 12)
# call a class method ,instance of the class can also be used to call the classmethod
print(Person.countObjects())

# calling the static method, instance of the class can also be used to call the staticmethod
Person.greet(7)
