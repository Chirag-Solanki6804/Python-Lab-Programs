## 05) WAP to find length of String without using len function.

name="chirag"

count=0
# for i in name:
#     count+=1

while name:
    count+=1
    name=name[1:]

print(count)