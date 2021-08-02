size=int(input())
st=list(map(int,input().split(' ')))
d={}
sum=count=0

#Processing
for i in st:
    if i<0:
        sum+=i
        count+=1
    
    else:
        d[sum]=count
        sum=count=0
        
d[sum]=count
mx=max(d.values())   


sum=0
for i in d.items():
    if i[1]==mx:
        sum+=i[0]
        
print(sum)