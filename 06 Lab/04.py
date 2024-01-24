# 4. WAP to interchange first and last elements in list entered by a user.

mylist=[]

number=0
while(number!=-1):
    print("Enter -1 for Stop")
    number=int(input("Enter a Number : "));
    if(number!=-1):
        mylist.append(number)
    
print("origin",mylist)
if len(mylist)>=2:
    # temp=mylist[0]
    # mylist[0]=mylist[len(mylist)-1]
    # mylist[len(mylist)-1]=temp
    mylist[0],mylist[-1]=mylist[-1],mylist[0]

print("output",mylist)


