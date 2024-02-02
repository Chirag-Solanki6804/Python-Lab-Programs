# 1. WAP to count even and odd numbers in a List.

mylist=[1,2,3,4,5,6,7,8,9,10]

eventCount=0

oddCount=0

for i in mylist:
    if i%2==0:
        eventCount+=1
    else:
        oddCount+=1

print("Event Count :",eventCount)
print("Odd Count :",oddCount)