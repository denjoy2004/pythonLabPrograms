class Rectangle:
    def __init__(self,length,breadth):
        self.length=length
        self.breadth=breadth
    def area(self):
        return self.length*self.breadth
    def perimeter(self):
        return 2*(self.length+self.breadth)
    def compare(self,other):
        if self.area()>other.area():
            print("First rectangle has larger area")
        elif self.area()<other.area():
            print("Second rectangle has larger area")
        else:
            print("Both recangle have equal area")
r1=Rectangle(10,5)
r2=Rectangle(6,4)
print("Area of the rectangle 1 : ",r1.area())
print("Area of the rectangle 2 : ",r2.area())
print("Perimeter of the rectangle 2 : ",r2.perimeter())
r1.compare(r2)