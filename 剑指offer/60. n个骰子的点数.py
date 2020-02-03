class Solution:
    def printProbability(self, n):
        if n < 1:
            return 0
        m = 6
        prob = [[0] * (m * n + 1) for _ in range(2)]
        flag = 0
        for i in range(1, m + 1):
            prob[flag][i] = 1
        for k in range(2, n + 1):
            for i in range(k):
                prob[1 - flag][i] = 0
            for i in range(k, m * k + 1):
                prob[1 - flag][i] = 0
                j = 1
                while j <= i and j <= m:
                    prob[1 - flag][i] += prob[flag][i - j]
                    j += 1
            flag = 1 - flag

        total = pow(m, n)
        result = []
        for i in range(n, m * n + 1):
            ratio = prob[flag][i] / total * 1.0
            result.append(ratio)
        return result


print(Solution().printProbability(2))
