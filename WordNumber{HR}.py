n=input().upper()
tot=sum=0

for i in n:
    tot=tot+(ord(i)-64)
    

if tot>9:    
    while tot>0:
        sum=sum+(tot%10)
        tot=tot//10
    
        if sum>9 and tot==0:
            tot=sum
            sum=0
    print(sum)
    
else:
    print(tot)
        