"""
给出一个序列包含n个正整数的序列A，然后给出一个正整数x，你可以对序列进行任意次操作的，
每次操作你可以选择序列中的一个数字，让其与x做按位或运算。
你的目的是让这个序列中的众数出现的次数最多。
请问众数最多出现多少次。
"""
def max_value(nums, x):
    count = {}
    for num in nums:
        count[num] = count.setdefault(num, 0) + 1
        ix = num | x
        if ix not in count:
            count[ix] = 1
        elif ix != num:
            count[ix] += 1
    return max(count.values())
n, x = map(int, input().split())
nums = list(map(int, input().strip().split()))
print(max_value(nums, x))
