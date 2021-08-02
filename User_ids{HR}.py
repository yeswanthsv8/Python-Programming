fn=input()
ln=input()
pin=int(input())
n=int(input())

p=str(pin)

if len(fn)==len(ln):
    l=[fn,ln]
    l=sorted(l)
    sma=l[0]
    lon=l[1]

elif len(fn)>len(ln):
    lon=fn
    sma=ln
    
else:
    lon=ln
    sma=fn
    

id=list(lon[0]+sma+p[n-1]+p[(-1)*n])
out=''


for i in id:
    if i.islower():
        out+=i.upper()
        
    elif i.isupper():
        out+=i.lower()
        
    else:
        out+=i

print(out)
