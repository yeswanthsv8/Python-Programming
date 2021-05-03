n=int(input())
s=[]
p=[]
w=[]
r=[]

if n>=1 and n<=10**5:
    for i in range(1,n*3+1):
        if i<=n:
            s.append(input())
            
        elif i<=n*2:
            p.append(int(input()))
        
        else:
            w.append(int(input()))
    
    for i in range(0,len(s)):
        r.append((s[i],p[i],w[i]))
        
    q=set(r)
    print(len(r)-len(q))
    
else:
    print(-1)