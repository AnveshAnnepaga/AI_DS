from abc import ABC, abstractmethod
# abstract classs
class Shape(ABC): 
    @abstractmethod
    def area(self):
        pass


class Rectangle(Shape):
    def __init__(self,len,bred):
        super().__init__()
        self.len=len
        self.bred=bred
    
    def area(self):
        ar=self.len*self.bred
        print("Area of rectangle is:",ar)

class Circle(Shape):
    def __init__(self,rad):
        super().__init__()
        self.rad=rad

    def area(self):
        a=3.14*self.rad*self.rad
        print("Area of circle is:",a)

r=Rectangle(2,4)
r.area()
c=Circle(5)
c.area()
