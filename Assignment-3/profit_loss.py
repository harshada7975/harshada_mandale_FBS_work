### WAP to calculate profit or loss

cp=int(input("enter the cost price:"))
sp=int(input("enter the selling price:"))


if(sp>cp):
    print(f"profit")
elif(cp>sp):
    print("loss")
else:
    print("not profit not loss")