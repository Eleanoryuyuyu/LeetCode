class Solution:
    def getPermutation(self, n: int, k: int) -> str:
        nums = list(range(1, n+1))
        fac = [1] * n
        res = ""
        for i in range(1, n):
            fac[i] = fac[i-1] * i
        k -= 1
        for i in range(n, 0, -1):
            ind = k // fac[i-1]
            k = k % fac[i-1]
            res += str(nums[ind])
            nums.remove(nums[ind])
        return res



print(Solution().getPermutation(4, 9))
