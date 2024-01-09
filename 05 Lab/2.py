## 2)WAP to print odd numbers between given two numbers.

num1= int(input("Enter a Number 1 ::"))

num2=int(input("Enter a Number 2 ::"))

while num1<=num2:
    if(num1%2!=0):
        print(num1)
    num1+=1