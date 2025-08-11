#### WAP to find the root of a quadratic equation.

a=int(input("enter the value of a:"))
b=int(input("enter the value of b:"))
c=int(input("enter the value of c:"))

sqrt=((b**2)-(4*a*c))**0.5
result1=(-b+sqrt)/(2+a)
result2=(-b-sqrt)/(2+a)

print(f"result1:{result1}")
print(f"result2:{result2}")


