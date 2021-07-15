n=int(input())
l=[]
for i in range(0,n):
    l.append(int(input()))

for i in range(0,len(l)//2):
             l[i],l[len(l)-1-i]=l[len(l)-1-i],l[i]
print(l)
        
