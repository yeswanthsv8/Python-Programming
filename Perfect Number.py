import math
def isprime(n):
    if n==0 or n==1:
        return False
    elif n>2 and n%2==0:
        return False
    else:
        max=math.floor(math.sqrt(n))
        for i in range(3,max+1,2):
            if n%i==0:
                return False
        return True
    
n=int(input())
b=bin(n)
b=b.replace('0b','')
b=len(b)

if(isprime(b)):
    print('Yes')
else:
    print('No')