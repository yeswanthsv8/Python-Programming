s=input()
par=sq=sc=0

for i in s:
    if i=='(':
        par+=1
        
    elif i==')':
        par-=1
        if par<0:
            sc+=1
            
    elif i=='[':
        sq+=1
    
    elif i==']':
        sq-=1
        if sq<0:
            sc+=1

if par==0 and sq==0 and sc==0:
    print(0)

elif par==0 and sq==0 and sc>0:
    print(sc)
    
else:
    print('-1')