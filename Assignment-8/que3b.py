def sum_fact(num):
    fact=1
    sum=0
    for i in range(1, num+1):
        fact *= i
        sum += fact
    return sum

num=int(input("enter the number :")) 
result=sum_fact(num)
print(f'factorial is {result}')