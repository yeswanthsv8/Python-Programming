import math
n1=int(input())
n2=int(input())
c=0

def isprime(i):
    if i==1:
        return False
    elif i==2:
        return True
    elif i>2 and i%2==0:
        return False
    else:
        max=math.floor(math.sqrt(i))
        for j in range(3,max+1,2):
            if i%j==0:
                return False
        return True

l=[i for i in range(1,n1+1) if (isprime(i))]

i=len(l)-1
while i>=0:
    if(n2%l[i]==0):
        c+=1
        n2=n2//l[i]
        i+=1
    if(n2==1):
        break
    else:
        i-=1
        
if(n2==1):
    print(c)
else:
    print('-1')
    
        
    