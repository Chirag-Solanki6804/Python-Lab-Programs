## 13) WAP to print all the number which are divisible by 11 but not divisible by 2 between given two numbers.

num1= int(input("Enter a Number 1 ::"))

num2=int(input("Enter a Number 2 ::"))

for num in range(num1,num2+1):
    if num%11==0 and num%2!=0:
        print(num)