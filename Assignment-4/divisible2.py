### WAP to find which number are divisible by 7 and multiple of 5 in given range.
start=int(input("enter the starting range:"))
end=int(input("enter the ending range:"))

for i in range(start,end+1):
    if(i%7==0 and i%5==0):
        print(i)