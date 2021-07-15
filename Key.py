n=int(input())
l=list(map(int,input().split(' ')))
key=int(input())
for i in l:
    if i<key:
        print(i,end=' ')

