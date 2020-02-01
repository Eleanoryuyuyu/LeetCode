class Solution:
    def GetTranslationCount(self, number):
        if number < 0:
            return 0
        str_number = str(number)
        length = len(str_number)
        counts = [0] * length
        for i in range(length - 1, -1, -1):
            if i < length - 1:
                count = counts[i + 1]
            else:
                count = 1
            if i < length - 1:
                dig1 = ord(str_number[i]) - ord('0')
                dig2 = ord(str_number[i + 1]) - ord('0')
                convert = dig1 * 10 + dig2
                if convert >= 10 and convert <= 25:
                    if i < length - 2:
                        count += counts[i + 2]
                    else:
                        count += 1
            counts[i] = count
        return counts[0]

print(Solution().GetTranslationCount(0))
