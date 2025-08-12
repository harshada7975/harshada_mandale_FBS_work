### WAP to print armstrong number within a given range.
num=int(input("enter the number:"))
temp=num
count=0
while(temp>0):
    count=count+1
    temp=temp//10

    sum=0
    while(temp>0):
        d=temp%10
        sum=sum+d**count
        temp=temp//10
if(num==sum):
    print(f"{num} is armstrong number.")
else:
    print(f"{num} is not armstrong number. ")