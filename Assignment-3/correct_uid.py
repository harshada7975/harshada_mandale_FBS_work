### WAP to check if user has entered correct userid and password.

uid=input("enter userid:")
password=int(input("enter the password:"))

if(uid=="admin" and password==1234):
    print(f"correct userid and password.")
else:
    print(f"not correct userid and password.")