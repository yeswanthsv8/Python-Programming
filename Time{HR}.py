n1=input()
n2=input()

l1=n1.split(':')
l2=n2.split(':')
l3=[00,00,00]

l1=list(map(int,l1))
l2=list(map(int,l2))

if(l1[2]>l2[2] or l1[2]==l2[2]):
    l3[2]=l1[2]-l2[2]

if(l1[2]<l2[2]):
    rea=60-l2[2]
    l2[2]=0
    l2[1]=l2[1]+1
    rem=l1[2]-l2[2]
    l3[2]=rem+rea

if(l1[1]>l2[1] or l1[1]==l2[1]):
    l3[1]=l1[1]-l2[1]

if(l1[1]<l2[1]):
    rea=60-l2[1]
    l2[1]=0
    l2[0]=l2[0]+1
    rem=l1[1]-l2[1]
    l3[1]=rem+rea
    
if(l1[0]>l2[0] or l1[0]==l2[0]):
    l3[0]=l1[0]-l2[0]

if(l1[0]<l2[0]):
    rea=l1[0]-l2[0]
    rea=abs(rea)
    l3[0]=24-rea

for i in range(0,len(l3)):
    if(len(str(l3[i]))==1):
        l3[i]='0'+str(l3[i])
    print(l3[i],end='')
    if(i!=2):
        print(':',end='')
    