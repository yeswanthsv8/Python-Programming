size=int(input())
l=[int(input()) for i in range(size)]
tsum=0

for i in l:
    mul=1
    for k in range(2,i):
        if i%k==0:
            mul*=k
    
    if mul==i:
        tsum+=mul
        
if tsum==0:
    print(-1)

else:
    print(tsum)