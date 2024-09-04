class Point :
    def __init__(self,a,b):
        self.a=a
        self.b=b

    def __add__(self,other) :
        return Point(self.a+other.a , self.b+other.b)
    
    def __str__(self):
        return f"Point({self.a}, {self.b})"

p1=Point(1,2)
p2=Point(4,6)

p3=p1+p2

print(p3)