
n = int(input())
items = [i+1 for i in range(n)]
result = [[]]
for x in items:
    result.extend([subset + [x] for subset in result])
res = 0
for cand in result:
    if len(cand)  == 1:
        res += 1
    elif len(cand) > 1:
        res += len(cand)
        res = res % (1e9+7)
print(int(res))