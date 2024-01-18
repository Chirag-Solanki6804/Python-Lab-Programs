## 12) WAP to print Fibonacci series up to number given by user.

num = int(input("Enter a Number"))

fiboSeries=[0,1];

while fiboSeries[-1]+fiboSeries[-2]<=num:
    fiboSeries.append(fiboSeries[-1]+fiboSeries[-2])

print(fiboSeries)
