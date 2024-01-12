## 5)  WAP to find whether the given number is prime or not.

num=int(input("Enter a Number :"))

idx=2

isPrime=True

if num<2:
    print("Not Prime Number")

while idx<num:
    if num%idx==0:
        isPrime=False
        break
    idx+=1

if isPrime:
    print(num,"is Prime Number")
else:
    print(num,"is not Prime Number")