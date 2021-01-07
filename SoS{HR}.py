n=int(input())

if n>9:
    sum=0
    flag=0
    l=list(str(n))
    for i in range(0,len(l)):
        for j in range(i,len(l)):
            sum+=int(l[j])
   
    for i in range(2,sum):
        if(sum%i==0):
            flag=1
            
    if(flag==0):
        while(sum>9):
            l=list(str(sum))
            sum=0
            for i in l:
                sum+=int(i)
        print(sum)
    else:
        print(sum)
else:
    print('-1')