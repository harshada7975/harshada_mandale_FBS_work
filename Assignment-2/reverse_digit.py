### WAP to reverse three digit number.

num=int(input("enter three digit number:"))
temp=num

d1=temp % 10
temp=temp // 10

d2=temp % 10
temp=temp // 10

d3=temp % 10
temp=temp // 10

 ###print(f"d1;{d1},d2:{d2},d3:{d3}")

reverse_digit=d1*100+d2*10+d3

print(f"revrese three digit is {reverse_digit}")