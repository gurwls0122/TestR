import sys
max_day = 0
case_count=1
L,P,V =map(int, sys.stdin.readline().split())

while L!=0 and P!=0 and V!=0:
    if V%P > L:
        max_day = (V//P) * L + L
    else:
        max_day =  (V//P) * L + V%P
    print("Case %d: %d" %(case_count, max_day))
    L, P, V = map(int, sys.stdin.readline().split())
    max_day = 0
    case_count+=1