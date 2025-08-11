#### WAP to check whether the triangle is equilateral or isosceles or scalene triangle.

a=int(input("enter the side a:"))
b=int(input("enter the side b:"))
c=int(input("enter the side c:"))

if((a==b) and (b==c) and (c==a)):
    print(f"equilateral triangle")
elif((a==b) or (b==c) or (c==a)):
    print(f"isosceles triangle")   
else:
    print(f"scalene triangle")     ## ((a!=b) and (b!=c) and (c!=a))
