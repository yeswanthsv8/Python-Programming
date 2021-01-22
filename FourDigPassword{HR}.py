s=input()
n=int(input())
l=[]
l1=[]

def sd(dif):
    sum=0
    while dif!=0 or sum>9:
        if dif==0:
            dif=sum
            sum=0
        sum+=dif%10
        dif//=10
    return sum

def odd(n):
    if n%2!=0:
        n+=1
    return n

up=0
lw=0
for i in s:
    if i.isupper():
        up+=1
        l1.append(i)
    elif i.islower():
        lw+=1
            
if(up>=2):
    v1=ord(l1[0])-64
    v2=ord(l1[1])-64
    dif=abs(v1-v2)
    l.append(sd(dif))

elif(up==1):
    v1=ord(l1[0])-64
    v2=0
    dif=abs(v1-v2)
    l.append(sd(dif))
        
else:
    l.append(0)

if lw>9:
    l.append(sd(lw))
else:
    l.append(lw)

if up>9:
    l.append(sd(up))
else:
    l.append(up)

if n>9:
    n=sd(n)
    l.append(odd(n))
else:
    l.append(odd(n))

for i in l:
    print(i,end='')