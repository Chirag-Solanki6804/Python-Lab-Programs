# 2. WAP to remove multiple elements from a list in Python as per value entered by user.

mylist=[1,3,4,5,6,7,8,9,10];

elem=mylist[0];

while elem!=-1:
    print(mylist);
    elem=int(input("Enter a Value You ant to delete Enter -1 to top:"));
    for i in range(0,len(mylist)):
        if mylist[i]==elem:
            ind=i
    mylist=mylist[:ind]+mylist[ind+1:]

    


