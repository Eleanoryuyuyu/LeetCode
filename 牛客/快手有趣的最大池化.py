"""
最近月神需要在移动端部署一个卷积神经网络模型,但是月神碰到了一个问题,即月神使用了一个核非常大的最大池化(max-pooling)操作,但现有推理引擎不支持这一操作,作为月神的好朋友,你能帮帮月神么。
所谓max-pooling,指的是给定一个数组（为了简化问题,暂定数组为一维）,在每一个滑动窗口内找出最大的那个数,举例如下：
假设数组为[16, 19, 15, 13, 16, 20],且核大小为3,则当窗口依次滑过数组时,取出如下4个子数组：
[16, 19, 15], [19, 15, 13], [15, 13, 16], [13, 16, 20],这4个子数组中的最大值分别为19, 19, 16, 20,故该数组经过大小为3的核的max-pooling的结果为19 19 16 20.
"""
n = int(input())
nums = list(map(int, input().split()))
w = int(input())

res = []
queue = []
for i in range(n):
    while queue and nums[i] > nums[queue[-1]]:
        queue.pop()
    queue.append(i)
    if i >= w-1:
        res.append(nums[queue[0]])
    if i - queue[0] + 1 == w:
            queue.pop(0)
res = [str(i) for i in res]
print(' '.join(res))

