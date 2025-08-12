### WAP to print fibonacci series uoto n.
num=int(input("enter the number:"))
a=1
b=0
for i in range(1,num):
    c=a+b
    print(c,end=' ')
    a=b
    b=c