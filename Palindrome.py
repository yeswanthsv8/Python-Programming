s=input()
j=len(s)-1
s1=''

while j>=0:
    s1+=s[j]
    j-=1
    
if s==s1: print('Palindrome')
else:
    print('Non Palindromef')
