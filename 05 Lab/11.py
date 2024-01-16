## 11) WAP to Find largest prime factor of given number.

num = int(input("Enter a Number :: ")) #18

maxPrime=0;
for i in range(2,num+1):
    if num%i==0:
        isPrime=True
        for j in range(2,i):
            if i%j==0:
                isPrime=False
                break
        if isPrime:
            if i>maxPrime:
                maxPrime=i
    
print("MaxPrime number ::",maxPrime)





