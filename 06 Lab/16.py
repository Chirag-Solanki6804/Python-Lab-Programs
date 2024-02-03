# 4. WAP to count the number of strings where the string length is 2 or more and the first and last character are same from a given list of strings.

mylist=["chiragc","solanki","helloh","hi","m"]

count=0

for string in mylist:
    if len(string)>=2:
        if string[0]==string[-1]:
            count+=1

print(count)