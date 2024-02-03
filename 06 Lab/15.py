# 3. WAP to print duplicates elements from a list of integers.

mylist=[1,1,2,3,3,4,5,6,7,7,8]

dup=[]

for i in mylist:
    if(mylist.count(i)>1) and (i not in dup):
        dup.append(i)

print(dup)