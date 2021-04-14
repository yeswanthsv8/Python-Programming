n=int(input())
l=list(map(int,str(n)))
s=''
sum=0
pas=1

first=l[0]
for i in range(0,len(l)):
    sum+=l[i]
   
    if pas>4:
        for j in range(i,len(l)):
            s=s+str(l[j])
        break
            
        
    elif (first%2!=0 and sum%2==0) or (first%2==0 and sum%2!=0) or (sum==l[i] and i==len(l)-1):
        s=s+str(sum)
        sum=0
        if i!=len(l)-1:
            first=l[i+1]
        pas+=1
    
    elif sum%2!=0 and i==len(l)-1:
        s=s+str(sum)

print(s)