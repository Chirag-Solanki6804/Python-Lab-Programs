## 01) WAP which accepts a string as input to print "Yes" if the string is "yes" or "YES" or "Yes", otherwise print "No".

name=input("Enter a name")

if(name.islower() or name.istitle() or name.isupper()):
    print("Ye")
else:
    print("No")

