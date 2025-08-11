###  WAP to enter p,t,r and calculate compound interest.

p=int(input("enter the value of amount:"))
t=int(input("enter the value of time:"))
r=int(input("enter the value of rate:"))

CI =p*(1+r)**t

print(f"compound interest is {CI}")