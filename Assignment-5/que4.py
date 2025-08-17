num=int(input("enter the number:"))
temp=num
power=0
while(temp>0):
    digit=temp%10
    power=power+digit**digit
    temp=temp//10

if(power==num):
    print(f"{num} is armstronge number.")
else:
    print(f"{num} is not armstrong number.")
    