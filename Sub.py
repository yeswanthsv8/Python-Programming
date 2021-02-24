s=input()
sub=input() 

for i in range(0,len(s)):
    if s[i]==sub[0]:
        k=i
        for j in range(0,len(sub)):
            if s[k]!=sub[j]:
                print('Not Found')
                break
            k+=1    
        else:
            print('Found at:',i)
                
                
        
