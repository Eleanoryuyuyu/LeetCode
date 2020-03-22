"""
一年一度的快手运动会又要开始了，同学们终于有一天可以离开鼠标键盘显示器，全身心的投入到各种体育项目中。UED设计师小红虽然没有参加体育项目，但她的责任重大，因为她是拉拉队的队长，她需要在每个项目中为参赛的同学们加油助威。

因为运动会的项目众多，很多项目在同一时间会同时进行着。作为拉拉队长，小红需要遵守以下规则：

不能同时给多个体育项目加油助威

给每个体育项目加油的时长必须超过项目时长的一半，每个体育项目只能加油一次

体育项目的开始和结束时间都是整点，如果项目进行到一半想要离开，也只能选择整点离开

不考虑往返于各个体育项目比赛场地中花费的时间

请帮小红设计一个算法，在已知所有体育项目日程的前提下，计算是否能在每个体育项目中为参赛的同学们加油。


说明：

如果体育项目时长为2，超过时长的一半为2;

如果体育项目时长为3，超过时长的一半为2;

如果体育项目时长为4，超过时长的一半为3；
"""

n = int(input())
metting = []
for _ in range(n):
    metting.append(list(map(int, input().split())))
time_list = []
for i in range(n):
    half = (metting[i][1] - metting[i][0])//2 + 1
    early_leave = metting[i][0] + half
    late_arr = metting[i][1] - half
    time_list.append([early_leave, late_arr])
time_list.sort(key=lambda x:x[1], reverse=True)
for i in range(n-1):
    if time_list[i][1] < time_list[i+1][0]:
        break
if i == n-2:
    print(1)
else:
    print(-1)