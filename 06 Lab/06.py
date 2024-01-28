# 6. WAP to reverses the list entered by user.  (any 3 ways)

mylist=[]

number=0
while(number!=-1):
    print("Enter -1 for Stop")
    number=int(input("Enter a Number : "));
    if(number!=-1):
        mylist.append(number)
    
print("origin",mylist)

# print(mylist[::-1])

# mylist.reverse()

start=0
end=len(mylist)-1

while start<end:
    mylist[start],mylist[end]=mylist[end],mylist[start]
    start+=1
    end-=1
print(mylist)