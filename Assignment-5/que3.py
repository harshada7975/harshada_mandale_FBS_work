passengers=int(input("enter the number of passengers: "))

ticket=int(input("enthe the ticket amount:"))

total_amount=0

for i in range(1,passengers+1):
    age=int(input("enter the age:"))

    if(age < 12):
        discount = ticket * 0.3
        amount = ticket - discount
    elif(age > 59):
        discount = ticket * 0.5
        amount = ticket - discount
    else:
        amount = ticket 

    total_amount += amount

print(f"total ticket amount is {total_amount}.")