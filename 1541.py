import sys
s = sys.stdin.readline().rstrip().split('-')
ans = 0
for i in range(len(s)):
    s[i] = s[i].split('+')
    result = 0
    for j in range(len(s[i])):
        result += int(s[i][j])
    s[i] = result
    if i==0:
        ans+=s[i]
    else:
        ans-=s[i]
print(ans)