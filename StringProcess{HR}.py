s=input()
input2=int(input())
input3=int(input())
s1=''

vowels='aeiouAEIOU'

#non-vowel and lowercase:
if input2==0 and input3==0:
    for i in s:
        if i not in vowels and i.islower():
            s1+=i

#non-vowel and uppercase:
elif input2==0 and input3==1:
    for i in s:
        if i not in vowels and i.isupper():
            s1+=i

#vowel and lowercase:
elif input2==1 and input3==0:
    for i in s:
        if i in vowels and i.islower():
            s1+=i

#vowel and uppercase:
elif input2==1 and input3==1:
    for i in s:
        if i in vowels and i.isupper():
            s1+=i

print(s1)