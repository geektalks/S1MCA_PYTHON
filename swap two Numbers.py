a=int(input("Enter number1: "))
b=int(input("enter number2: "))
print("Swaping using temp")
print("a before swaping",a)
print("b before swaping",b)
temp=a
a=b
b=temp
print("a after swaping",a)
print("b after swaping",b)
print("Without using temp")
a=int(input("Enter number1: "))
b=int(input("enter number2: "))
print("a before swaping",a)
print("b before swaping",b)
a=a+b
b=a-b
a=a-b
print("a after swaping",a)
print("b after swaping",b)
