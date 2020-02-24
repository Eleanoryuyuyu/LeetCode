def find_lcsubstr(str1, str2):
    n = len(str1)
    m = len(str2)
    if n == 0 or m == 0:
        return ""
    dp = [[0] * (m+1) for _ in range(n+1)]
    max_len = 0
    end = 0
    for i in range(1, n+1):
        for j in range(1, m+1):
            if str1[i-1] == str2[j-1]:
                dp[i][j] = dp[i-1][j-1] + 1
            if dp[i][j] > max_len:
                max_len = dp[i][j]
                end = i
    return str1[end-max_len:end]

str1 = input()
str2 = input()
print(find_lcsubstr(str1, str2))