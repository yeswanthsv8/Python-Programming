n=int(input())

while n>=10:
    n//=10
if n%2==0:
    print('Even')
else:
    print('Odd')
