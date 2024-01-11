## 4) WAP to print sum of digits of given number.

num = int(input("Enter a Number :"))

add=0
while num>0:
    digit=num%10;
    add+=digit
    num=int(num/10);

print(add)

