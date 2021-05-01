size=int(input())
l=[int(input()) for i in range(0,size)]

mx=max(l)
mn=min(l)

for i in range(0,len(l)):
    if mn<=mx and l.index(mn)<l.index(mx):
        result=mx-mn
        print(result)
        break

    else:
        if l.index(mx)!=0:
            if len(l)>1:
                l.remove(mn)
                mn=min(l)
            else:
                print(-1)
                break
            
        else:
            if len(l)>1:
                l.remove(mx)
                mx=max(l)
            else:
                print(-1)
                break
            
else:
    print(-1)
    