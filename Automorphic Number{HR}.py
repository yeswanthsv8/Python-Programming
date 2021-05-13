n=int(input())
sq=n**2

sq=str(sq)
n=str(n)
c=0

j=-1
for i in range(len(n)-1,-1,-1):
    if n[i] in sq[j]:
        c+=1
    j-=1
        
if c==len(n):
    print('true')
else:
    print('false')
    
    
   