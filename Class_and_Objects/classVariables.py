class Person:
    # class variable
    count = 0

    def __init__(self, name):
        self.name = name
        # add one to 'count' every time the init is called
        Person.count += 1
        # can also access like this: 'self.count'

# Creates two instances of the 'Person' class
p1 = Person("niya")
p2 = Person("rinu")

# Access the class variable using the class
print(Person.count)
# Access the class variable using an object
print(p1.count)
