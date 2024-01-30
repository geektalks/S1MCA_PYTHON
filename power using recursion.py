def power(b,e):
    if e==0:
        return 0
    elif e==1:
        return b
    else:
        return b*power(b,e-1)
b=int(input("Enter the base: "))
e=int(input("Enter the power: "))
result=power(b,e)
print(result)
