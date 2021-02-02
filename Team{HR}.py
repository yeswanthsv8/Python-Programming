n=input()
r=''
sample='pcmbz'
out=0

if len(n)<5:
    print('0')
    
else:
    i=0
    while i<len(n):
        if n[i] not in r and n[i] in sample:
            r=r+n[i]
            n=n.replace(n[i],'',1)
        
        else:
            i+=1
            
        if len(r)==5:
            out+=1
            i=0
            r=''
print(out)        