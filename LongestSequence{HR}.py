n=int(input())
l=[int(input()) for i in range(0,n)]
result=[]

count=1
for i in range(0,len(l)):
    
    if i!=len(l)-1 and l[i]<l[i+1]:
        count+=1
    
    elif count>1:
        result.append(count)
        count=1
    
    if count==len(l):
        print(count)
        break

else:
    if len(result)>0:
        print(max(result))
    else:
        print(0)