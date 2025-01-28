# 2975. Maximum Square Area by Removing Fences From a Field

from typing import List

class Solution:

    def findMax(self, hFences, vFences):
            
        while True:

            if len(hFences) < 1 or len(vFences) < 1:
                break

            h = hFences.pop()
            v = vFences.pop()

            if h < v:
                hFences.append(h)
            if v < h:
                vFences.append(v)
            if h == v:
                return (h*v) % (10 ** 9 + 7)

        return -1

    def maximizeSquareArea(self, m: int, n: int, hFences: List[int], vFences: List[int]) -> int:
        
        hFences.append(1)
        vFences.append(1)
        hFences.append(m)
        vFences.append(n)
        hFences = sorted(hFences)
        vFences = sorted(vFences)

        all_h_diff = set()
        for i in range(0, len(hFences)):
            for j in range(i+1, len(hFences)):
                all_h_diff.add(hFences[j]-hFences[i])

        all_v_diff = set()
        for i in range(0, len(vFences)):
            for j in range(i+1, len(vFences)):
                all_v_diff.add(vFences[j]-vFences[i])

        all_h_diff = sorted(list(all_h_diff))
        all_v_diff = sorted(list(all_v_diff))

        # print(all_h_diff)
        # print(all_v_diff)
        return self.findMax(all_h_diff, all_v_diff)



m_1 = 4
n_1 = 3
hFences_1 = [2,3]
vFences_1 = [2]
# Output: 4
# Explanation: Removing the horizontal fence at 2 and the vertical fence at 2 will give a square field of area 4.

m_2 = 6
n_2 = 7
hFences_2 = [2]
vFences_2 = [4]
# Output: -1
# Explanation: It can be proved that there is no way to create a square field by removing fences.

m_3 = 3
n_3 = 9
hFences_3 = [2]
vFences_3 = [8,6,5,4]
# Output:  4

m_4 = 5
n_4 = 3
hFences_4 = [4]
vFences_4 = [2]
# Output 1

print(Solution().maximizeSquareArea(m_1, n_1, hFences_1, vFences_1))
print(Solution().maximizeSquareArea(m_2, n_2, hFences_2, vFences_2))
print(Solution().maximizeSquareArea(m_3, n_3, hFences_3, vFences_3))
print(Solution().maximizeSquareArea(m_4, n_4, hFences_4, vFences_4))

