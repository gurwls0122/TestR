import sys
N = int(sys.stdin.readline())
if N < 100:
    print(N)
else:
    count = 99
    for i in range(100, N+1):
        if i//100 - (i%100)//10 == (i%100)//10 - i%10:
            count+=1
        else:
            continue
    print(count)