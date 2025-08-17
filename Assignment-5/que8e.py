n=int(input("enter the number of n :"))
x=int(input("enter the number of x :"))
sum=0
for i in range(1,n+1):
    s= ((-1)**(i+1)) * (x**i) / (2*i-1)
    sum += s
print(f"sum of series : {sum} ")