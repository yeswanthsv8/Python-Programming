s=input()
op=0
cl=0

for i in s:
    if i=='(':
        op+=1
    else:
        cl+=1
        if(cl>op):
            print('-1')
            exit()
if(cl==op):
    print(cl)
else:
    print('-1')
        
