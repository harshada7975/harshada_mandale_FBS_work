#### WAP to convert days into year,week and days.

days=int(input("enter the days:"))

year= days // 365

days= days % 365

week= days // 7

days= days % 7

print(f"{year}year, {week}weeks, {days}days")