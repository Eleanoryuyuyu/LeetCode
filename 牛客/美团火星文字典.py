def get_order(words):
    unique = set()
    order_dic = {}
    unique.update(list(words[0]))
    for i in range(1, len(words)):
        pre = words[i-1]
        cur = words[i]
        unique.update(list(cur))
        short = min(len(pre), len(cur))
        for j in range(short):
            if pre[j] != cur[j]:
                if pre[j] not in order_dic and cur[j] not in order_dic.values():
                    order_dic[pre[j]] = cur[j]
                break
    res = words[0][0]
    k = words[0][0]
    while order_dic.get(k):
        v = order_dic[k]
        if v in order_dic and k == order_dic[v]:
            return "invalid"
        res += v
        k = v
    if len(res) != len(unique):
        return "invalid"
    return res

words = list(input().strip().split())
print(get_order(words))
