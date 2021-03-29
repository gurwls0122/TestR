import sys
count = 0
S = list(sys.stdin.readline().rstrip())
for i in range(len(S)-1):
    if S[i] != S[i+1]:
        count+=1
    else:
        continue
if count%2 == 0:
    result = count//2
else:
    result = count//2 +1
print(result)