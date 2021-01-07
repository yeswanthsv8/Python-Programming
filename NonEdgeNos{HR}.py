x=int(input())
y=int(input())
sum=0

if x>2 and y>2:
    for i in range(0,x):
        for j in range(0,y):
            if(i!=0 and i!=x-1 and j!=0 and j!=y-1):
                sum+=int(input())
            else:
                input()
    print(sum)
else:
    print(-1)