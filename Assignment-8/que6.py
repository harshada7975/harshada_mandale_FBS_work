def fibbonacci(num):
    a=1
    b=0
    for i in range(1,num+1):
        c=a+b
        print(c,end=' ')
        a=b
        b=c
    
    return c
n=int(input("enter the number of n :"))
result=fibbonacci(n)
print(f"fibbonacci series : {result}")

