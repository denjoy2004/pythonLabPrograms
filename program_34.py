class Rectangle:
    def __init__(self,length,width):
        self.length=length
        self.width=width
    def area(self):
        return self.length*self.width
    def __lt__(self,other):
        return self.area()<other.area()
r1=Rectangle(10,5)
r2=Rectangle(6,4)
if r1<r2:
    print("Rectangle 1 has smaller area")
else:
    print("Rectangle 1 has greateer area or equal")
print("Area oif the Recrangle 1 : ",r1.area())
print("Area oif the Recrangle 2 : ",r2.area())
