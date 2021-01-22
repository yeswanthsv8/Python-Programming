import math
def isprime(n):
    if n==0 or n==1:
        return False
    
    elif n==2:
        return True
    
    elif n>2 and n%2==0:
        return False
    
    else:
        max=math.floor(math.sqrt(n))
        for j in range(3,max+1,2):
            if n%j==0:
                return False
        return True
    
n=int(input())
sum=0
l=[int(input()) for i in range(0,n)]

for i in range(0,len(l)):
    if(not isprime(i)):
        sum+=l[i]
print(sum)