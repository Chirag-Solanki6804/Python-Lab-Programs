## 04) WAP to print even length word in string

name=input("Enter a String ::")

words=name.split(" ")

# for word in words:
#     if len(word)%2==0:
#         print(word)

index=0

while index<len(words):
    if len(words[index])%2 == 0:
        print(words[index])
    index+=1



