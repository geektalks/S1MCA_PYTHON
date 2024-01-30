def pal(n):
    if n==n[::1]:
        return("YES")
    else:
        return("NO")
num=input("Enter the number: ")
result=pal(num)
print(result)
