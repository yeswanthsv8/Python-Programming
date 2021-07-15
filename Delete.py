n=int(input())
l=[]
for i in range(0,n):
    l.append(int(input()))

key=int(input())
for i in range(0,len(l)):
    if l[i]==key: 
        for j in range(i,len(l)-1):
            l[j]=l[j+1]
        l[j+1]=None

print(l)
