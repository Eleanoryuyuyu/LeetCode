
def bigAdd(a, b):
    if not a:
        return b
    if not b:
        return a
    res = []
    l = min(len(a), len(b))
    a = a[::-1]
    b = b[::-1]
    flag = 0
    i = 0
    for i in range(l):
        c = int(a[i]) + int(b[i]) + flag
        res.append(str(c % 10))
        flag = c //10
    if i < len(a)-1:
        res.extend(a[i+1:])
    elif i < len(b)-1:
        res.extend(b[i+1:])
    res = list(reversed(res))
    return ''.join(res)

num1, num2 = input().split()
print(bigAdd(num1, num2))


