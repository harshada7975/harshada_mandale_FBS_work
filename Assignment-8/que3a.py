def sum_series(num):
    s=0
    for i in range(1, n+1):
        s += i
    return s
    
n=int(input("enter the number of n :"))
result=sum_series(n)
print(f"sum of series : {result}")
    