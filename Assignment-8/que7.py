def sum_digit(num):
    sum=0
    while(num>0):
        d= num%10
        sum += d
        num= num//10

    return sum

n=int(input("enter the number of n :"))
result=sum_digit(n)
print(f"sum of digits:{result}")