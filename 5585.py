import sys
count = 0
money= [500, 100, 50, 10, 5, 1]
pay = 1000 - int(sys.stdin.readline())
for i in money:
    if pay < i:
        continue
    else:
        count += pay//i
        pay= pay%i
print(count)