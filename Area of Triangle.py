print("Area of a triangle")
a=float(input("Enter side1: "))
b=float(input("Enter side2: "))
c=float(input("Enter side3: "))
s=(a+b+c)/2
area=(s*(s-a)*(s-b)*(s-c))**0.5
print(area)
