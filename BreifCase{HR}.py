import string
s=string.ascii_lowercase

cases=int(input())
l=[input() for i in range(cases)]

for i in l:
    l1=i.split(' ')
    fir=l1[0]
    sec=l1[1]
    
    count=0
    for j in range(0,len(fir)):
        if j!=len(fir)-1:
            if int(fir[j+1])-int(fir[j])==count:
                count=0
            elif int(fir[j+1])-int(fir[j])>count:
                count=1
                break
            else:
                count=-1
                break
    
    ans=sum(list(map(int,fir)))
    result=''
    if count==1:
        tot=ans-1
        for i in range(1,int(sec)+1):
            result+=s[tot]
            tot+=1
        
    elif count==-1:
        tot=ans*-1
        for i in range(1,int(sec)+1):
            result+=s[tot]
            tot-=1
    else:
        for i in range(1,int(sec)+1):
            result+=s[int(fir[1])-1]
    
    print(result)
    