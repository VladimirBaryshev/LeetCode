# 1291. Sequential Digits

from typing import List

class Solution:

    def sequentialDigits(self, low: int, high: int) -> List[int]:
        
        s = "123456789"

        l = len(str(low))
        h = len(str(high))

        r = []
        for i in range(l,h+1):
            j = 0
            while j+i < 10:
                print(s[j:j+i])
                if (int(s[j:j+i]) <= high) and (int(s[j:j+i]) >= low):
                    r.append(int(s[j:j+i]))
                j += 1

        return r


low_1 = 100
high_1 = 300
# Output: [123,234]

low_2 = 1000
high_2 = 13000
# Output: [1234,2345,3456,4567,5678,6789,12345]

low_3 = 58
high_3 = 155
# [67,78,89,123]

# print(Solution().sequentialDigits(low_1, high_1))
# print(Solution().sequentialDigits(low_2, high_2))
print(Solution().sequentialDigits(low_3, high_3))




