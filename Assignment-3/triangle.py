### WAP to input angle of tringle and check whether tringle is vaild or not. 
angle1=int(input("enter the angle:"))
angle2=int(input("enter the angle:"))
angle3=int(input("enter the angle:"))

if(angle1+angle2+angle3==180):
    print(f"angle is triangle ")
else:
    print(f"angle is not tringle")