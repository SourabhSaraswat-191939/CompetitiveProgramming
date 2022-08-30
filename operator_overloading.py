class complex:
    def __init__(self, a):
        self.a = a
 
     # adding two objects
    def __sub__(self, other):
        return self.a * other.a
 
Ob1 = complex(2)
Ob2 = complex(6)
Ob3 = Ob2 - Ob1
print(Ob3)