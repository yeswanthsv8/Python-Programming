n=input().lower()
s=''

for i in n:
    s+=str(ord(i)-96)

while len(s)>1:
    sum=0
    for i in s:
        sum+=int(i)**2
    if sum<10:
        break
    s=str(sum)
print(sum)