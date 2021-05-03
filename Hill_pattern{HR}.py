rows=int(input())
head=int(input())
inc=int(input())
sum=pre=0

lim=1
for i in range(1,rows+1):
    for j in range(1,lim+1):
    
        if j%2==0:
            sum+=pre
            
        else:
            sum+=head
            
    pre=head
    head=head+inc
    lim+=2

print(sum)
    