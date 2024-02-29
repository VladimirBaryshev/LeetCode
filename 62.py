# 62. Unique Paths
# https://leetcode.com/problems/unique-paths/description/

def uniquePaths(m: int, n: int) -> int:
    
    stack = [(0,0)]
    m -= 1
    n -= 1

    count = 0

    while stack:

        cur_y, cur_x = stack.pop()

        if cur_y < m:
            stack.append((cur_y+1, cur_x))
        if cur_x < n:
            stack.append((cur_y, cur_x+1))
        if cur_y == m and cur_x == n:
            count += 1

    return count


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





