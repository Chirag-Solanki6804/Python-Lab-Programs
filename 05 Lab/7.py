## 7) WAP to print sum of series 1–2+3–4+5–6+7...n

limit = int(input("Enter a Number :: "))

# for i in range(limit):
#     print(i)

# print("********************************************")

# for i in reversed(range(limit)):
#     print(i)

ans=0
for i in range(1,limit+1):
    if i%2==0:
        ans=ans-i;
    else:
        ans=ans+i;

print(ans)

