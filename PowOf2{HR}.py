from math import *
def pow(n):
    if n==0:
        return False
    
    else:
        return floor(log2(n))==ceil(log2(n))
        
size=int(input())
l=[int(input()) for i in range(size)]

for i in l:
    if pow(i):
        print(1)
    else:
        print(0)
            