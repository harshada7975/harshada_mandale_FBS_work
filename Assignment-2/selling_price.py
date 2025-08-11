#### WAP to calculate selling price of book based on cost price and discount.

cp=int(input("enter costprice of book :"))
dis=int(input("enter discount of book : "))

dis_amount = (dis/100) * cp

sp= cp - dis_amount

print(f"selling price of book is {sp}")