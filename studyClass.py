
class dog(object):
    def __init__(self,name,age ):
        self.name = name
        self.age = age

    def speak(self):
        print(f"Hi i am {self.name} and i am {self.age} years old")

    def change_name(self,name):
        self.name = name
me = dog("niya",13)
someone = dog("noone", 14)
me.speak()
someone.change_name("someone")
someone.speak()