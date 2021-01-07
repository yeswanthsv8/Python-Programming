amt=int(input())
l=[]

tw=amt//2000
amt=amt%2000

th=amt//1000
amt=amt%1000

f=amt//500
amt=amt%500

h=amt//100
amt=amt%100

if amt==0:
    l1=[tw,th,f,h]
else:
    l1=[-1,-1,-1,-1]


print('[',end='')
for i in range(0,len(l1)):
    print(l1[i],end='')
    if(i==3):
        print(']')
    else:
        print(',',end='')
        