n=input()
val=0

while True:
    val=sum(list(map(int,n)))
    if(int(n)%val)==0:
        n=int(n)//val 
        if val<10:
            print(n)
            break
        else:
            n=str(n)
            
    elif(int(n)%val)>0:
        n='-'+n
        print(n)
        break