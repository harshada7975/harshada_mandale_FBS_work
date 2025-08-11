
salary=int(input("enter the salary:"))

da_amount=salary*0.1   #da_salary=salary*(1/100)
ta_amount=salary*0.12
hra_amount=salary*0.15

total_salary=salary+da_amount+ta_amount+hra_amount

print(f"total salary is {total_salary}")