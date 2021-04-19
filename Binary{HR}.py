n=int(input())
l=[int(input()) for i in range(0,n)]


j=sum=0
for i in range(len(l)-1,-1,-1):
    sum=sum+l[i]*pow(2,j)
    j+=1
print(sum)