## 03) WAP to remove ith character from given string.

name = input("Enter your name :")

index=int(input("Enter index you want to delete :"))

name = name[:index]+name[index+1:]

print(name)

