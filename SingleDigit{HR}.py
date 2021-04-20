n=int(input())
sum=0

while n>0:
    sum=sum+pow(n%10,2)
    n=n//10
    
    if sum>9 and n==0:
        n=sum
        sum=0

print(sum)
