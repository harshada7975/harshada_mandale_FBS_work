amount=int(input("enter the amount : "))

notes=[2000, 500, 200, 100, 50, 10]
total_notes=0

for note in notes:
    if(amount >= note):
        count = amount // note
        amount = amount % note
        total_notes += count
    
print(f" total no.of notes : {total_notes}")    