num=int(input("Enter a Number to check Happy :"))
temp=num
while(num>9):
    total=0
    while(num>0):
        digit=num%10
        total+=digit**2
        num=num//10
    num=total
    print(num)

if num==1:
    print(temp,"is Happy number")
else:
    print(temp,"is Not Happy Number")

    



