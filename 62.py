# 62. Unique Paths
# https://leetcode.com/problems/unique-paths/description/

def uniquePaths(m: int, n: int) -> int:
    
    stack = [(0,0)]
    coords = []
    costs = dict()

    for y in range(m):
        for x in range(n):
            coords.append((y,x))

    for y,x in coords[::-1]:
        if y+1 == m or x+1 == n:
            costs[(y,x)] = 1
        else:
            costs[(y,x)] = costs[(y+1,x)] + costs[(y,x+1)]

    return costs[(0,0)]



m_1 = 3
n_1 = 7
# Output: 28
        
m_2 = 3
n_2 = 2
# Output: 3
# Explanation: From the top-left corner, there are a total of 3 ways 
# to reach the bottom-right corner:
# 1. Right -> Down -> Down
# 2. Down -> Down -> Right
# 3. Down -> Right -> Down

m_3 = 23
n_3 = 12

print(uniquePaths(m_1, n_1))
print(uniquePaths(m_2, n_2))
print(uniquePaths(m_3, n_3))





