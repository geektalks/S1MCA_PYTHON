print("Arithmetic Operations")
n1=float(input("Enter the first number:"))
n2=float(input("Enter the second number:"))
op=input("+,-,/,*")
if op=="+":
  result= n1+n2
elif op=="-":
  result= n1-n2
elif op=="/":
  result= n1/n2
elif op=="*":
  result= n1*n2
else:
  print("INVALID CHOISE")
print(result)
