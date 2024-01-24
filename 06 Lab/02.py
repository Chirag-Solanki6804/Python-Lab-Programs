# 2. WAP to find the smallest and largest element in a list.

mylist=[5,10,15,20,12,13,8,2]


smallest=mylist[0]
largest=mylist[0]
for i in mylist:
    if(i<smallest):
        smallest=i
    if(i>largest):
        largest=i

print("smallest :",smallest)
print("largest :",largest)