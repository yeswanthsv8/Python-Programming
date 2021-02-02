n=int(input())
l=[int(input()) for i in range(0,n)]
out=0

mx=max(l)
mxi=l.index(mx)

if mxi>0:
    mn=min(l[0:mxi])
    out=mx-mn
    
else:
    l.remove(mx)
    for i in l:
        if max(l)!=l[0]:
            mx=max(l)
            mxi=l.index(mx)
            mn=min(l[0:mxi])
            out=mx-mn
            break
        else:
            l.remove(max(l))

if out==0:
    print('-1')
else:
    print(out)


