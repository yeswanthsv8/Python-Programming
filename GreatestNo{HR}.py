s=int(input())
l=[]

if s<0:
    s=s*-1
    
while s!=0:
    rem=s%10
    l.append(rem)
    s=s//10
    
if(len(l)>=2 and len(l)<=5):
    l.sort(reverse=True)
    for i in l:
        print(i,end='')

elif len(l)==1:
    print('-1')

else:
    print('9')