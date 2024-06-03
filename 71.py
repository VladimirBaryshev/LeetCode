# 71. Simplify Path
# https://leetcode.com/problems/simplify-path/description/


class Solution:

    def simplifyPath(self, path: str) -> str:
        
        path = path.split("/")

        res = []

        for p in path:
            if p == "..":
                if res:
                    res.pop()
            elif p.isalpha() or (p and p != "."):
                res.append(p)

        return "/" + "/".join(res)



path_1 = "/home/"
# Output: "/home"
# Explanation:
# The trailing slash should be removed.

path_2 = "/home//foo/"
# Output: "/home/foo"
# Explanation:
# Multiple consecutive slashes are replaced by a single one.

path_3 = "/home/user/Documents/../Pictures"
# Output: "/home/user/Pictures"
# Explanation:
# A double period ".." refers to the directory up a level.

path_4 = "/../"
# Output: "/"
# Explanation:
# Going one level up from the root directory is not possible.

path_5 = "/.../a/../b/c/../d/./"
# Output: "/.../b/d"
# Explanation:
# "..." is a valid name for a directory in this problem.        

print(Solution().simplifyPath(path_1))
print(Solution().simplifyPath(path_2))
print(Solution().simplifyPath(path_3))
print(Solution().simplifyPath(path_4))
print(Solution().simplifyPath(path_5))

