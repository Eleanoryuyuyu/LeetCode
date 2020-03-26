def bigSub(str1, str2):
    num1 = [int(i) for i in str1]
    num2 = [int(i) for i in str2]
    res = ""
    for i in range(len(num2)):
        index1 = len(num1) -i -1
        index2 = len(num2) -i -1
        if num1[index1] >= num2[index2]:
            res = str(num1[index1] - num2[index2]) + res
        else:
            res = str(10 + num1[index1] - num2[index2]) + res
            while num1[index1-1] != 0:
                num1[index1-1] = 9
                index1 -= 1
            num1[index1] -= 1
    res = str1[:len(num1)-len(num2)] + res

    zeroflag = 0
    for i in range(len(res)):
        if res[i] != '0':
            zeroflag = 1
            break
    if zeroflag == 0:
        return 0
    return res[i:]

str1, str2 = input().split()
print(bigSub(str1, str2))

