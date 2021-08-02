no=int(input())
s1=input()
s2=input()
res=[]

for i in range(0,no):
    if s1[i]=='.':
      res.append(0)
    
    elif s1[i]!=s2[i]:
        res.append(1)
        
    elif s1[i]==s2[i]:
        res.append(0)
        
    else:
        res.append(1)
        
print(sum(res))
    