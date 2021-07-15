n=int(input())
l=list(map(int,input().split(' ')))
m=l[0]
for i in l:
    if i>m:
        m=i
print(m)
