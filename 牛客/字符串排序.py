"""
生活中经常有需要将多个字符串进行排序的需要，比如将美团点评的部分业务名称（外卖、打车、旅游、丽人、美食、结婚、旅游景点、教培、门票、酒店），
用拼音表示之后按字母逆序排序。字母逆序指从z到a排序，比如对两个字符串排序时，
先比较第一个字母按字母逆序排z在a的前面，当第一个字母一样时再比较第二个字母按字母逆序排，
以此类推。特殊情况1)空字符串需排在最前面；
2)若一个短字符串是另一个长字符串的前缀则短字符串排在前面。
请自行实现代码进行排序，直接调用sort等排序方法将不得分且视为作弊。
"""

def compare(str1, str2):
    if not str1:
        return True
    if not str2:
        return False
    for i in range(min(len(str1), len(str2))):
        if str1[i] > str2[i]:
            return True
        elif str1[i] < str2[i]:
            return False
    return True if len(str1) < len(str2) else False

strings = input().split(',')
for i in range(len(strings)):
    for j in range(i, len(strings)):
        if compare(strings[j], strings[i]):
            strings[i], strings[j] = strings[j], strings[i]
print(','.join(strings))