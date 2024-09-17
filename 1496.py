# 1496. Path Crossing

class Solution:

    def isPathCrossing(self, path: str) -> bool:
        
        moves = {
                    "N": (1,0),
                    "E": (0,1),
                    "S": (-1,0),
                    "W": (0,-1)
                }

        log = set()
        cur = (0,0)
        log.add(cur)

        for p in path:
            y,x = cur
            p = moves[p]
            y += p[0]
            x += p[1]

            if (y,x) in log:
                return True

            log.add((y,x))
            cur = (y,x)

        return False
            

path_1 = "NES"
# Output: false 
# Explanation: Notice that the path doesn't cross any point more than once.

path_2 = "NESWW"
# Output: true
# Explanation: Notice that the path visits the origin twice.
 

print(Solution().isPathCrossing(path_1))
print(Solution().isPathCrossing(path_2))


