s=input()
s1=''
vowels=['a','e','i','o','u','A','E','I','O','U']
for i in s:
    if i not in vowels:
        s1+=i
print(s1)
