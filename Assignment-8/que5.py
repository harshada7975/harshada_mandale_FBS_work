def sum_prime(n):
    num=2
    count=0

    while(count<n):
        for i in range(2, num):
            if(i%2 == 0):
                break
        else:
            print(num,end=' ')
            count += 1
        num += 1
          
        return num

n=int(input("enter the number of n :"))
result=sum_prime(n)
print(f"sum of prime number :{result}")
