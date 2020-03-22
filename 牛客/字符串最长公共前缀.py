"""
第1行输入一个整数n，代表字符串数量；

第2~n+1行，每行一个字符串；

第n+2行开始，每行输入两个整数a和b，代表需要计算公共前缀的字符串编号。
输入：
2
abc
abe
1 2
输出
2
"""


import sys
n = int(input())
strings = []
for i in range(n):
    strings.append(input().strip())
index = []
for line in sys.stdin:
#py.3中input（）只能输入一行  sys.stdin按下换行键然后ctrl+d程序结束
    list_new = list(map(int, line.split()))
    index.append(list_new)
for line in index:
    a, b = line[0], line[1]
    str1 = strings[a-1]
    str2 = strings[b-1]
    n, m = len(str1), len(str2)
    l = min(n, m)
    res = 0
    for i in range(l):
        if str1[i] == str2[i]:
            res += 1
        else:
            break
    print(res)