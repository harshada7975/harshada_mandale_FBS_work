### WAP to accept an integer amount from user and tell minimun number of notes needed representing that amount.

amount = int(input("enter the amount :"))

temp=amount

two_thousand = temp // 2000
temp = temp % 2000

five_hundred = temp // 500 
temp = temp % 500

two_hundred = temp // 200
temp = temp % 200

hundred = temp // 100
temp = temp % 100

fifty = temp // 50
temp = temp % 50

twenty = temp // 20
temp = temp % 20

ten = temp // 10
temp = temp % 10

total_notes = two_thousand + five_hundred + two_hundred + hundred + fifty  + twenty + ten

print(f" total no.of notes : {total_notes}")