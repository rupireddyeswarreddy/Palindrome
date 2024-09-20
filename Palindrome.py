#Two Ways of printing a Palindrome

#Known Way
a=input()
ans=''
n=len(a)
for i in range(n-1,-1,-1):
    ans+=a[i]
if ans==a:
    print('palindrome')
else:
    print('not a palindrome')


#Unknown (most people)
ans='abcdba'
n=len(ans)//2
mul = len(ans)
valid=True
for i in range(3):
    l=ans[i]
    r=ans[mul-i-1]
    if l!=r:
        valid = False
    print(l,r)
if valid:
    print('yes')
else:
    print('no')
