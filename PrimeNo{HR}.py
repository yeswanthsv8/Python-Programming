import math
def primeNO(n):
        if n==0 or n==1:
            return False
        
        elif n==2:
            return True
            
        elif n>2 and n%2==0:
            return False
    
        else:
            max=math.floor(math.sqrt(n))
            for i in range(3,max+1,2):
                if n%i==0:
                    return False
            return True
                
                    

n1=int(input())
n2=int(input())
l=[]
sum=0

for i in range(1,n1+1):
    if primeNO(i):
        l.append(i)
        
i=len(l)-1
while i>=0:
    if n2%l[i]!=0:
        i-=1;
        
    else:
        n2=n2//l[i]
        sum+=1
 
    if n2==1:
        print(sum)
        break

else:
    print(-1)

        
    