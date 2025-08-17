n=int(input("enter the number of n :"))
sum=0
exp=1
for i in range(1, n+1):
    sum= sum + (n**i)

print(f"sum of series = {sum}")