def leap_year(year):
    if((year % 4 == 0) or (year % 100 != 0) and (year % 400 == 0)):
        return True
    else:
        return False

y=int(input("enter a year : "))
result=leap_year(y)
if(result):
    print(f"{y} is a leap year.")
else:
    print(f"{y} is not a leap year.")