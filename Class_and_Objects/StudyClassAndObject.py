class Person():
    # method: function inside a class that can be called upon objects.
    # self : refer to the instance of the class
    def __init__(self,name, age):
        # attributes: variables that serve as a peoperty of the object.
        self.name = name
        self.age = age
        

    def Greeting(self):
        print(f"Hello!, I'm {self.name} and i am {self.age} years old")

    def New_age(self, newAge):
        self.age = newAge    

# Object is a piece of data made from a class ,with its own properties and methods of its class.
p1 = Person("niya",13)
p1.Greeting()

# another object of the class person()
p2 = Person("lofi",12)

# printing the attributes
print(p1.name)

p1.New_age(43)
p1.Greeting()