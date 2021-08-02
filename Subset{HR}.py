size=int(input())
l=[int(input()) for i in range(size)]
count=0
res=[]

for i in range(size):
    for j in range(0,size):
        if l[i]<l[j] and (l[i]+l[j])%2!=0:
            res.append((l[i],l[j]))
     
s=set(res)
print(len(s))