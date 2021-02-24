s=input() 
sub=input() 

count=0
for i in range(0,len(s)):
    if s[i]==sub[0]:
        k=i
        for j in range(0,len(sub)):
            if s[k]!=sub[j]:
                break
            k+=1    
        else:
            count+=1
print(count)            
                
        
