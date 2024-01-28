# 5. WAP to interchange the list elements on two positions entered by a user from a list.

mylist=[1,2,3,4,5,6,7]

pos1=int(input("Enter posotion 1 :"))
pos2=int(input("Enter posotion 2 :"))

if (pos1>-1 and pos1<len(mylist)) and (pos2>-1 and pos2<len(mylist)):
    mylist[pos1],mylist[pos2]=mylist[pos2],mylist[pos1]
else:
    print("Enter Valid posotion")

print(mylist) 

