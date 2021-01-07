n=int(input())
l=list(map(int,input().split(' ')))
l1=[]

for i in l:
    if i not in l1:
        l1.append(i)

        
c=0
for j in l1:
    if l.count(j)>1:
        c+=1 
print(c)