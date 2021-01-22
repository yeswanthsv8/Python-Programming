n=int(input())
l=[int(input()) for i in range(0,n)]

l1=l.copy()
l2=l.copy()
inc=0
de=0

for i in range(0,len(l)-1):    
    #increasing order
    if not l1[i]<=l1[i+1]:
        inc+=abs(l1[i+1]-l1[i])
        l1[i+1]=l1[i]
    
    #decreasing order
    if not l2[i]>=l2[i+1]:
        de+=abs(l2[i]-l2[i+1])
        l2[i]=l2[i+1]
if inc<=de:
    print(inc)
else:
    print(de)