n=int(input())

if(n>9):
    a=str(n)
    add=0
    flag=0
    ans=0
    
    for i in range(len(a)):
        add=add+(int(a[i])*(i+1))
    
    for i in range(2,add//2):
        if add%i==0:
            flag=1
            break
            
    if(flag==0):
        while(add!=0):
            rem=add%10
            ans=ans+rem
            add=int(add/10)
        
        if(ans<10):
            print(ans)
        else:
            add=ans
            ans=0
            while(add!=0):
                rem=add%10
                ans=ans+rem
                add=int(add/10)
            print(ans) 
            
    else:
        print(add)       
    
else:
    print("Not Able to Process.")
    