#### WAP to input all side of tringle and check whether tringle is valid or not.
s1=int(input("enter the tringle side:"))
s2=int(input("enter the tringle side:"))
s3=int(input("enter the tringle side:"))

if((s1+s2)>s3 and (s1+s3)>s2 and (s2+s3)>s1):
    print(f"tringle is valid")
else:
    print(f"tringle is not valid") 