n=int(input())
out=[]

def Greater(ice,c):
    if ice>0:
        l[i]=l[i]+1
        ice-=1
        
    else:
        l[i]=l[i]-1
        ice+=1
        c+=1
    return ice,c

def Smaller(ice):
    if ice>0:
        l[i]=l[i]+1
        ice-=1
    
    else:
        l[i]=l[i]+1
        ice-=1
    return ice

for i in range(0,n):
    size=int(input())
    l=list(map(int,input().split(' ')))
    ice=c=0 
    
    for i in range(0,len(l)):
        if i%2==0:
            if l[i]%2!=0 and l[i]>=2:
                ice,c=Greater(ice,c)           
                    
                
            elif l[i]%2!=0 and l[i]<2:
                ice=Smaller(ice)
                
        else:
            if l[i]%2==0 and l[i]>=2:
                ice,c=Greater(ice,c)       
                
            elif l[i]%2==0 and l[i]<2:
                ice=Smaller(ice)
                
    if ice==0:
        out.append(c)
    else:
        out.append(-1)
        
for i in out:
    print(i)