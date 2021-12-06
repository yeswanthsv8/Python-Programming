cases=int(input())
l=[input() for i in range(cases)]
t_alp=26

for i in l:
    if '?' in i:
        if len(i)==2:
            print('0')
            
        elif len(i)==1:
            print(t_alp)
        
        else:
            if i.index('?')==len(i)-1 or i.index('?')==0:
                print('1')
                
            else:
                print(t_alp-(len(i)-2))
            
    else:
        if len(i)==2:
            if i[0]==i[-1]:
                print('0')
                
        elif len(i)==1:
            print('1')
            
        else:
            for k in range(0,len(i)):
                if k!=len(i)-1 and i[k]==i[k+1]:
                    print('0')
                    break
            else:
                if i[0]!=i[-1]:
                    print('0')
        
                else:
                    print('1')
            