# 8. WAP to print all odd number in list entered by user.

mylist=[]

number=0
while(number!=-1):
    print("Enter -1 for Stop")
    number=int(input("Enter a Number : "));
    if(number!=-1):
        mylist.append(number)
    
print("origin",mylist)

for i in mylist:
    if i%2!=0:
        print(i)