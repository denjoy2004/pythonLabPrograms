square=lambda side:side*side
rectangle=lambda lenght,breadth:lenght*breadth
tirangle=lambda base ,height:0.5*base*height
side=float(input("Enter the side of the sqaure : "))
print("Area of square : ",square(side))
lenght=float(input("Enter the lenght of the rectangle : "))
breadth=float(input("Enter the breadth of the rectangle : "))
print("Area of rectangle : ",rectangle(lenght,breadth))
base=float(input("Enter the base of the triangle : "))
height=float(input("Enter the height of the triangle : "))
print("Area of the triangle : ",tirangle(base,height))



