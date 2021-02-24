s1=input()
s2=input()
if len(s1)==len(s2):
    for i in range(0,len(s1)):
        if s1[i]!=s2[i]:
            print('Not Equal')
            break
    else:
        print('Equal')
else:
    print('Not Equal')
