### WAP to print prime number between 1 to 100.
count=0
num=2

for i in range(2,101):
    for i in range(2,num):
        if(num%i==0):
            break
    else:
        print(num,end=' ')
        count=count+1
    num=num+1