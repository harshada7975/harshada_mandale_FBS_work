def revers_num(num):
    rev=0
    while(num>0):
        d= num%10
        rev= rev * 10 + d
        num= num//10
    return rev
n=int(input("enter the number of n :"))
result=revers_num(n)
print(f"reverse of number :{result}")