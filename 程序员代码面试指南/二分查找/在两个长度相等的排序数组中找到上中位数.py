def findMid(n, arr1, arr2):
    if n == 1:
        return arr1[0] if arr1[0] < arr2[0] else arr2[0]
    s1, e1, s2, e2 = 0, n-1, 0, n-1
    while s1 < e1:
        mid1 = (e1-s1)//2 + s1
        mid2 = (e2-s2)//2 + s2
        # 元素个数为奇数，则offset=0， 元素个数为偶数， 则offset=1
        offset = ((e1-s1+1) & 1) ^1
        if arr1[mid1] > arr2[mid2]:
            e1 = mid1
            s2 = mid2 + offset
        elif arr1[mid1] < arr2[mid2]:
            s1 = mid1 + offset
            e2 = mid2
        else:
            return arr1[mid1]
    return min(arr1[s1], arr2[s2])

n = int(input())
a = list(map(int, input().split()))
b = list(map(int, input().split()))
print(findMid(n, a, b))
