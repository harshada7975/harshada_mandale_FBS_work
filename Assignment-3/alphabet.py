#### WAP to input any alphabet and check whether it vowel or consonant. 
alpha=input("enter the alphabet:")

if(alpha  in "aeiouAEIOUE" ):
    print(f"{alpha} is vowel")
else:
    print(f"{alpha} is consonant")