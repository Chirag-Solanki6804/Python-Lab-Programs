## 02) WAP to find all duplicate characters in string.

name="chirag solanki"

i=0;

myli=[]
while i<len(name):
    if name[i] not in myli and name.count(name[i])>1:
        myli.append(name[i])
    i+=1

print(myli);