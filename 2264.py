# 2264. Largest 3-Same-Digit Number in String



class Solution:

    def largestGoodInteger(self, num: str) -> str:
        
        d = {
            "999": 10,
            "888": 9,
            "777": 8,
            "666": 7,
            "555": 6,
            "444": 5,
            "333": 4,
            "222": 3,
            "111": 2,
            "000": 1
        }

        result = -1

        for i in range(2, len(num)):
            if num[i-2:i+1] in d.keys():
                result = max(d[num[i-2:i+1]], result)

        if result == -1:
            return ""

        return [(k,v) for k,v in d.items() if v == result][0][0]



num_1 = "6777133339"
# Output: "777"
# Explanation: There are two distinct good integers: "777" and "333".
# "777" is the largest, so we return "777".

num_2 = "2300019"
# Output: "000"
# Explanation: "000" is the only good integer.

num_3 = "42352338"
# Output: ""
# Explanation: No substring of length 3 consists of only one unique digit. 
# Therefore, there are no good integers.

num_4 = "222"
# Output: "222"

print(Solution().largestGoodInteger(num_1))
print(Solution().largestGoodInteger(num_2))
print(Solution().largestGoodInteger(num_3))
print(Solution().largestGoodInteger(num_4))


