class Solution:
    def MaxDiff(self, numbers):
        if len(numbers) < 2:
            return 0
        min_num = numbers[0]
        max_num = 0
        for i in numbers[1:]:
            diff = i - min_num
            if diff > max_num:
                max_num = diff
            if i < min_num:
                min_num = i
        return max_num

numbers = [9, 11, 8, 5, 7, 12, 16, 14]
print(Solution().MaxDiff(numbers))