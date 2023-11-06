class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    
    def greeting(self):
        print(f"hello! i am {self.name} and i'm {self.age} years old")

# inheriting the Person class
class Student(Person):
    def __init__(self, name, age, grade):
        # 'super().' method is refering to the parent's "__init__()" 
        super().__init__(name, age)
        self.grade = grade  
    
    def greeting(self):
        # calls the parent's greeting method using 'super().'
        super().greeting()
        # overrides the parent's method with the same name with it's own method
        print(f"hello! i am {self.name} and i'm {self.age} years old, In {self.grade} grade")
    
st1 = Student("niya fathima", 12, "8th")
st1.greeting()