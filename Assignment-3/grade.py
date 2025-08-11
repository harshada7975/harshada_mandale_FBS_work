### WAP to input 5 subject marks from user and disply grade.

m1=int(input("entre the marks of subject 1:"))
m2=int(input("entre the marks of subject 2:"))
m3=int(input("entre the marks of subject 3:"))
m4=int(input("entre the marks of subject 4:"))
m5=int(input("entre the marks of subject 5:"))

gain_marks=m1+m2+m3+m4+m5
percentage=(gain_marks/500)*100

if(percentage>=75):
    print(f"first class with {percentage}%")
elif(percentage>=55):
    print(f"second class with {percentage}%")
elif(percentage>=35):
    print(f"pass with {percentage}%")
else:
    print(f"fail")


