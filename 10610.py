import sys
n = sys.stdin.readline().rstrip()
is_True = False
new_lst = []
for i in range(len(n)):
    new_lst.append(n[i])

sum = 0
for i in new_lst:
    if int(i) == 0:
        is_True = True
    sum+=int(i)
if is_True == False or sum%3!=0:
    print(-1)
else:
    new_lst.sort(reverse=True)
    print(''.join(new_lst))