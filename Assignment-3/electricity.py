### WAP to input electricity unit charges and calculate total electricity bill.

units=int(input("enter the electricity units :"))

if(units <= 50):
    bill = units * 0.50
elif(units <= 150):
    bill = units * 0.75
elif(units <= 250):
    bill = units * 1.20
else:
    bill = units * 1.50

surcharge = bill * 0.20
total_bill= bill + surcharge

print(f"electricity bill is {total_bill}.")