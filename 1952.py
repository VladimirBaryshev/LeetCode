# 1952. Three Divisors


class Solution:

    def isThree(self, n: int) -> bool:

        r = []

        for i in range(1, n+1):
            if n % i == 0:
                r.append(i)

        if len(r) == 3:
            return True
        else:
            return False

        



n_1 = 2
# Output: false
# Explantion: 2 has only two divisors: 1 and 2.

n_2 = 4
# Output: true
# Explantion: 4 has three divisors: 1, 2, and 4.

print(Solution().isThree(n_1))
print(Solution().isThree(n_2))
print(Solution().isThree(1))
print(Solution().isThree(10000))

        