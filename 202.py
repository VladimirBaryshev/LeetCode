# 202. Happy Number
# https://leetcode.com/problems/happy-number/description/

def isHappy(n: int) -> bool:
    
    visited = set()

    while n not in visited and n != 1:
        visited.add(n)
        n = str(n)
        n = sum([int(i)**2 for i in n])

    if n == 1:
        return True
    return False


n_1 = 19
# Output: true
# Explanation:
# 1**2 + 9**2 = 82
# 8**2 + 2**2 = 68
# 6**2 + 8**2 = 100
# 1**2 + 0**2 + 0**2 = 1

n_2 = 2
# Output: false

print(isHappy(n_1))
print(isHappy(n_2))
