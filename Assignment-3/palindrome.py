#### WAP to ckeck if given3 digit number is a palindrome or not

num=int(input("enter three digit number:"))
temp=num

d1=temp % 10
temp=temp // 10

d2=temp % 10
temp=temp // 10

d3=temp % 10
temp=temp // 10

rev_num=(d1*100)+(d2*10)+d3

if(num==rev_num):
    print(f"{rev_num} is not polindrome")
else:
    print(f"{rev_num} is polindrome ")


