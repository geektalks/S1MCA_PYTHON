n= int(input("Enter the number of students: "))
names=[]
for i in range(n):
    name=input("Enter the name: ")
    names.append(name)
print("The list before sorting:",names)
print("The list after sorting:")
for j in range(n):
    a=sorted(names)
    print(a[j])
