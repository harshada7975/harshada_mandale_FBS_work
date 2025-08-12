### WAP to check if given number is strong number.
num=int(input("enter the number:"))
temp=num
i=1
sum=0
fact=0
while(temp>0):
    d=temp%10
    temp=temp//10
    while(i<=d):
        fact *= i
        i += 1
    sum += fact
        
if(sum==num):
    print(f"{num} is strong")
else:
    print(f"{num} is not strong")