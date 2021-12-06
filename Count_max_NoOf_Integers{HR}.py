from itertools import combinations

lim=int(input())
l=[int(input()) for i in range(lim)]
tot=int(input())
r=[]

if tot in l:
    r.append(1)
    
for i in range(2,lim+1):
    for j in combinations(l,i):
        if sum(j)==tot:
            r.append(len(j))
            

if len(r)==0:
    print(-1)
else:
    print(max(r))