# 10. WAP to sort a list in ascending or descending order as per user’s choice.

mylist=[1,5,2,6,4,9,5,8,22,54,21]

# number=0
# while(number!=-1):
#     print("Enter -1 for Stop")
#     number=int(input("Enter a Number : "));
#     if(number!=-1):
#         mylist.append(number)
    
print("origin",mylist)

choice=int(input("Enter 0 for ascending or Enter 1 for descending ::"))

if(choice==0):
    # mylist.sort()
    # print(mylist)
    for i in range(len(mylist)):
        for j in range(len(mylist)-i-1):
            if(mylist[j]>mylist[j+1]):
                mylist[j],mylist[j+1]=mylist[j+1],mylist[j]
else:
    # mylist.sort()
    # mylist.reverse()
     for i in range(len(mylist)):
        for j in range(len(mylist)-i-1):
            if(mylist[j]<mylist[j+1]):
                mylist[j],mylist[j+1]=mylist[j+1],mylist[j]
       
print(mylist)