def sum_odd(num):
    total=0
    for i in range(1,num+1):
        if((i%2) != 0):
            total += i
    return total
n=int(input("enter the number of n :")) 
result=sum_odd(n)
print(f"sum of add numbers :{result}")
