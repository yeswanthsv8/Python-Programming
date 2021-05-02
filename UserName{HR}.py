size=int(input())
l=[input().lower() for i in range(0,size)]

s=set(l)

for i in s:
    if l.count(i)>1:
        st=l.index(i)
        c=0
        for j in range(st+1,len(l)):
            if l[j]==i:
                c+=1
                l[j]=l[j]+str(c)
        
for i in l:
    print(i)
                
            