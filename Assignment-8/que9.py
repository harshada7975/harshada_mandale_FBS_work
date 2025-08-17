def palindrome(num):
    temp=num
    rev=0
    while(num>0):
        d= num%10
        rev= rev * 10 + d
        num= num//10
    return temp==rev
    
n=int(input("enter the number of n :"))
result=palindrome(n)
if(result):
    print(f"{n} is a palindrome ")
else:
    print(f"{n} is not a palindrome")