# 788. Rotated Digits


class Solution:
    def rotatedDigits(self, n: int) -> int:
        
        d = {
            "1" : "1",
            "0" : "0",
            "8" : "8",
            "2" : "5",
            "5" : "2",
            "6" : "9",
            "9" : "6"
        }

        r = set()

        for i in range(1, n+1):
            try:
                candidate = "".join(d[i] for i in str(i))
                if candidate != str(i):
                    r.add(candidate)
            except KeyError:
                continue

        return len(r)


n_1 = 10
# Output: 4
# Explanation: There are four good numbers in the range [1, 10] : 2, 5, 6, 9.
# Note that 1 and 10 are not good numbers, since they remain unchanged after rotating.

n_2 = 1
# Output: 0

n_3 = 2
# Output: 1

print(Solution().rotatedDigits(n_1))
print(Solution().rotatedDigits(n_2))
print(Solution().rotatedDigits(n_3))