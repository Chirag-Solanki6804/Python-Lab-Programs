# 5. WAP to check whether a list contains a sub-list and generate all sub-lists of a list.

myli=[1,3,4,5,6,7,8,9,0];

li=[8,0,9]

gf=False
for i in range(len(myli)):
    for j in range(i+1,len(myli)+1):
        if myli[i:j]==li:
            gf=True
            break
if gf:
    print("oo yEE")
else:
    print("oooohh no")