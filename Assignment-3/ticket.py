
age1=int(input("entre the age of person 1 :"))
age2=int(input("enter the age of person 2 :"))
age3=int(input("enter the age of person 3 :"))
age4=int(input("enter the age of person 4 :"))
age5=int(input("enter the age of person 5 :"))

ticket=int(input("enter the ticket amount :"))

### person 1 
if(age1 < 12):
    discount = ticket * 0.3
    amount1 = ticket - discount
elif(age1 > 59):
    discount = ticket * 0.5
    amount1 = ticket - discount
else:
    amount1 = ticket 

### person 2
if(age2 < 12):
    discount = ticket * 0.3
    amount2 = ticket - discount
elif(age2 > 59):
    discount = ticket * 0.5
    amount2 = ticket - discount
else:
    amount2 = ticket

### person 3
if(age3 < 12):
    discount = ticket * 0.3
    amount3 = ticket - discount
elif(age3 > 59):
    discount = ticket * 0.5
    amount3 = ticket - discount
else:
    amount3 = ticket

### person 4
if(age4 < 12):
    discount = ticket * 0.3
    amount4 = ticket - discount
elif(age4 > 59):
    discount = ticket * 0.5
    amount4 = ticket - discount
else:
    amount4 = ticket

### person 5
if(age5 < 12):
    discount = ticket * 0.3
    amount5 = ticket - discount
elif(age5 > 59):
    discount = ticket * 0.5
    amount5 = ticket - discount
else:
    amount5 = ticket

total_amount = amount1 + amount2 + amount3 + amount4 + amount5
print(f"total amount is {total_amount}")
