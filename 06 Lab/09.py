# 9. WAP to search an element in a list as entered by user.

mylist=[]

number=0
while(number!=-1):
    print("Enter -1 for Stop")
    number=int(input("Enter a Number : "));
    if(number!=-1):
        mylist.append(number)
    
print("origin",mylist)

search=int(input("Enter Element for search in list :"))

for i in range(len(mylist)):
    if(search==mylist[i]):
        print(search,"found at index",i)
        break
else:
    print("search element Not found")