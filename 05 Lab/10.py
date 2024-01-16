## 10) WAP to find out prime numbers between given two numbers.

start=int(input("Enter a Start Number :"))

end=int(input("Enter a End Number :"))

while start<=end:
    if start<2:
        start+=1
        continue
        
    isPrime=True
    for i in range(2,start):
        if start%i==0:
            isPrime=False
            break
    if isPrime:
        print(start,"is prime")
    start+=1;