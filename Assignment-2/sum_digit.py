### WAP to find the sun of three digit number

num=int(input("enter three digit number:"))
temp=num

d1=temp % 10
temp=temp // 10

d2=temp % 10
temp=temp // 10

d3=temp % 10
temp=temp //10

print(f"d1;{d1},d2:{d2},d3:{d3}")

sum=d1+d2+d3

print(f"{num} is {sum}")