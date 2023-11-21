#adding arguments to the function beforehand
# --> the code won't crash

def func(name, age=0):
    return f"you are {name} and you are {age} years old"

call1 = func("niya",13)
# print(call1)





class Car():
    def __init__(self, company, model, year=0000, condition="New"):
        self.company = company
        self.model = model
        self.year = year
        self.condition = condition

    def displayCar(self):
        return f"This is a {self.company} {self.model} from {self.year}, and its a {self.condition} car"
    
car1 = Car("Lamborgini", "Aventador", 2013)
print(car1.displayCar())