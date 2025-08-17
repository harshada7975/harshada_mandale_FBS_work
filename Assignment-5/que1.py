attempts=3
for i in range(1,attempts+1):
    userid=input("enter the userid:")
    password=int(input("enter the password:"))
    
    if(userid=="admin" and password==1234):
        print(f"login succesfully")
        break
    else:
        print(f"incoreect userid and password. attempts left:{attempts-i}")

