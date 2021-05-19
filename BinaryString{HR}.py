n=int(input())
l=[int(input()) for i in range(0,n)]

for i in l:
    s=str(i)
    c=sum=0
    for j in s[::-1]:
        sum+=int(j)*pow(2,c)
        c+=1
    
    if sum==1:
        print('true')
    
    else:
        while sum!=1:
            if sum%2==0:
                sum=sum/2
                if sum==1:
                    print('true')
                    break

            else:
                print('false')
                break
            
            