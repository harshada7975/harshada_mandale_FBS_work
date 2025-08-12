### to print all numbers in arange divisible by a given number.
start=int(input("enter the number:"))
stop=int(input("enter the number:"))
div=int(input("enter the number:"))

for i in range(start,stop+1):
    if(i % div == 0):
        print(i)