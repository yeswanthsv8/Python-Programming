s=input()
ch=input()
for i in s:
    if i==ch:
        print(s.index(i))
        break
else:
    print('Not Found')
