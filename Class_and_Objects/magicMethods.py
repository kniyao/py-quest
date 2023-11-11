class Value:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    # adds two object
    def __add__(self, v):
        return Value(self.x + v.x, self.y + v.y)
    
    # subtracts two object
    def __sub__(self, v):
        return Value(self.x - v.x, self.y - v.y)
    
    # multiplies two object
    def __mul__(self, v):
        return Value(self.x * v.x, self.y * v.y)
    
    # devides two object
    def __truediv__(self,v):
        return Value(self.x / v.x, self.y / v.y)
    
    # returns the value of the object as string
    def __str__(self):
        return f"{str(self.x)}, {str(self.y)}"


class Compare:
    def __init__(self, i, j):
        self.i = i
        self.j = j
    # compares two objects

    def __eq__(self, c):
        return self.i == c.i and self.i == c.i
    
    def __gt__(self, c):
        return self.i > c.i and self.j > c.j
    
    def __lt__(self, c):
        return self.i < c.i and self.j < c.j
    
    def __ge__(self, c):
        return self.i >= c.i and self.j < c.j
    
    def __le__(self, c):
        return self.i <= c.i and self.j < c.j

class MyList:
    def __init__(self, items):
        self.items = items
    # returns the length of the object
    def __len__(self):
        return len(self.items)

p1 = Value(5,6)
p2 = Value(7,7)

print(p1 + p2)
print(p1 - p2)
print(p1 * p2)
print(p1 / p2)

c1 = Compare(3,3)
c2 = Compare(5,5)
c3 = Compare(4,8)
c4 = Compare(6,9)

print(c1 == c2)
print(c4 < c1)
print(c3 > c4)
print(c4 > c3)

item1 = MyList(["apple","banana","orange","papaya"])
item2 = MyList([1,2,3,4,5,6,7,8])

print(len(item1))
print(len(item2))
