size=int(input())
l=[int(input()) for i in range(0,size)]
occ=0

if size==0:
    print(occ)

s=set(l)
for i in s:
    if l.count(i)>1:
        occ+=1
print(occ)
