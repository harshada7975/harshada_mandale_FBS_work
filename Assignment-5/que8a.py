n=int(input('enter the number on n :'))
fact=1
sum=0
for i in range(1, n+1):
    fact *= i
    sum += fact

print(f'sum of series = {sum}')