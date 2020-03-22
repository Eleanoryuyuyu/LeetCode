n = int(input())
a = list(map(int, input().split()))
b = list(map(int, input().split()))

bag = []
for i in range(n):
    bag.append([a[i], b[i]])
bag = sorted(bag, key=lambda x: x[1],reverse=True)
v = sum(a)
k, tmp, cur = 0, 0, 0
for i in range(n):
    if cur >= v:
        break
    cur += bag[i][1]
    k += 1
    tmp += bag[i][0]
t = v - tmp

print(str(k) + ' '+ str(t))