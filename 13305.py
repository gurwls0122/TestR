import sys
result = 0
N = int(sys.stdin.readline())
dis = list(map(int, sys.stdin.readline().split()))   #거리
oil = list(map(int, sys.stdin.readline().split()))  #각 도시의 리터당 기름값

result += oil[0]*dis[0]
min_oil = oil[0]
for i in range(1, N-1):
    if oil[i] < min_oil:
        min_oil = oil[i]
    else:
        oil[i] = min_oil
    result += oil[i]*dis[i]
print(result)