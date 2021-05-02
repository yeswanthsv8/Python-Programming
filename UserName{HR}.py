size=int(input())
l=[input() for i in range(0,size)]
l1=[]

for i in l:
    l1.append(i.lower())

s=set(l)

for i in s:
    if l1.count(i)>1:
        st=l1.index(i)
        c=0
        for j in range(st+1,len(l)):
            if l1[j]==i:
                c+=1
                l[j]=l[j]+str(c)
        
for i in l:
    print(i)
                
            