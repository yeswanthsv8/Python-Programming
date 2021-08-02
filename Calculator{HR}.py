import re
size=int(input())
l=[input() for i in range(size)]

#[24+87,(87)248+204,(8)+(6)+9)]
sym='+-*/()%'

for i in l:
    if re.findall('\A[*/)%]',i) or i.count('(')!=i.count(')') or i[-1] in sym:
        print('Invalid')
        
    else:
        for j in range(0,len(i)):
            if i[j]==')' and i[j+1] not in sym:
                print('Invalid')
                break
                
        else:
            print('Valid')
                