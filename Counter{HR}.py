from collections import Counter as c
size=int(input())
l=[int(input()) for i in range(size)]
d={}
l.sort()

for i in l:
    d.update({i:l.count(i)})
    
d=dict(sorted(d.items(),key=lambda x:x[1],reverse=False))
res=c(d).elements()

for i in res:
    print(i)

