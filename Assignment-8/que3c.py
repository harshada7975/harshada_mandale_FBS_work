def sum_power(n):
    sum=0
    for i in range(1, n+1):
        k = i**i
        sum += k
    return sum
n=int(input("enter the number :"))
result=sum_power(n)
print(f"sum of series :{result}")