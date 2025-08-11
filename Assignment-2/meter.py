### convert distant given in feet and inches into meter and centimeter.

feet=int(input("enter distance in feet :"))
inches=int(input("enter distance in inches :"))

total_inches = (feet * 12) + inches

centimeter = total_inches * 2.54

meter = centimeter // 100
centimeter = centimeter % 100

print(f"merter = {meter} and centimete = {centimeter}")