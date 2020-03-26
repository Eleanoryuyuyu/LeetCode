
def bigMutil(str1, str2):
    num1, num2 = int(str1), int(str2)
    if num1 == 1:
        return num2
    elif num2 == 1:
        return num1
    res = 0
    pos = 1
    if len(str1) < len(str2):
        str1, str2 = str2, str1
        num1, num2 = num2, num1
    for i in str2[::-1]:
        res += num1 * int(i) * pos
        pos *= 10

    return res

str1, str2 = input().split()
print(bigMutil(str1, str2))
