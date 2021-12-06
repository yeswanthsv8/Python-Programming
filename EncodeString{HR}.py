def D3(s):
    spt=len(s)//3
    st=s[0:spt]
    
    val=-1*spt
    mid=s[spt:val]
    sp=s[val:]
    return [st,mid,sp]
    
def L4(s):
    st=s[0]
    sp=s[-1]
    s=s.replace(st,'')
    mid=s[0:-1]
    return [st,mid,sp]
    
def N_D3(s):
    spt=len(s)//2
    rem=len(s)-spt*2
    if spt-rem<3:
        pass
    else:
        spt=(len(s)//2)-1
        
    st=s[0:spt]
    
    val=-1*spt
    sp=s[val:]
    s=s.replace(st,'')
    s=s.replace(sp,'')
    mid=s[:]
    return [st,mid,sp]

s1=input()
s2=input()
s3=input()

#String 1:
if len(s1)%3==0:
    sep1=D3(s1)
    
elif len(s1)==4:
    sep1=L4(s1)
    
else:
    sep1=N_D3(s1)
    
#String 2:
if len(s2)%3==0:
    sep2=D3(s2)
    
elif len(s2)==4:
    sep2=L4(s2)
    
else:
    sep2=N_D3(s2)
        

#String 3:
if len(s3)%3==0:
    sep3=D3(s3)
    
elif len(s3)==4:
    sep3=L4(s3)
    
else:
    sep3=N_D3(s3)
    
i=0
j=i+1
k=i+2

for i in range(0,len(sep1)):
    st=sep1[i]
    
    if j>2:
        j=0
    elif k>2:
        k=0
        
    mid=sep2[j]
    sp=sep3[k]
    j+=1
    k+=1
    
    print(st+mid+sp)