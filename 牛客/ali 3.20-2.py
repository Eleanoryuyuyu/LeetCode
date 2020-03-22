
n = int(input())
strings = []
for i in range(n):
    s = input()
    strings.append(s)

strings.sort()

dp = [0] * 26
for i in range(n-1, -1, -1):
    cur = strings[i]
    head_pos = ord(cur[0]) - ord('a')
    tail_pos = ord(cur[-1]) - ord('a')
    for j in range(tail_pos, 26):
        dp[head_pos] = max(dp[head_pos], dp[j] + len(cur) )


print(max(dp))

