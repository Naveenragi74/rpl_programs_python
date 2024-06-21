a = str(input())
c={}
for chr in a:
    if chr in c:
        c[chr]+=1
    else:
        c[chr]=1
print(c)