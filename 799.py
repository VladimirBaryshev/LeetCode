# 799. Champagne Tower

class Solution:

    def champagneTower(self, poured: int, query_row: int, query_glass: int) -> float:

        tower = [[0] * (i + 1) for i in range(query_row + 1)]
        tower[0][0] = poured

        for row in range(query_row):
            for glass in range(len(tower[row])):
                excess = (tower[row][glass]-1) / 2.0
                if excess > 0:
                    tower[row+1][glass] += excess
                    tower[row+1][glass+1] += excess

        return min(1, tower[query_row][query_glass])



poured_1 = 1
query_row_1 = 1
query_glass_1 = 1
# Output: 0.00000
# Explanation: We poured 1 cup of champange to the top glass of the tower (which is indexed as (0, 0)).
# There will be no excess liquid so all the glasses under the top glass will remain empty.

poured_2 = 2
query_row_2 = 1
query_glass_2 = 1
# Output: 0.50000
# Explanation: We poured 2 cups of champange to the top glass of the tower (which is indexed as (0, 0)). 
# There is one cup of excess liquid. The glass indexed as (1, 0) and the glass indexed as (1, 1) 
# will share the excess liquid equally, and each will get half cup of champange.

poured_3 = 100000009
query_row_3 = 33
query_glass_3 = 17
# Output: 1.00000

poured_4 = 25
query_row_4 = 6
query_glass_4 = 1
# Expected 0.18750

print(Solution().champagneTower(poured_1, query_row_1, query_glass_1))
print(Solution().champagneTower(poured_2, query_row_2, query_glass_2))
print(Solution().champagneTower(poured_3, query_row_3, query_glass_3))
print(Solution().champagneTower(poured_4, query_row_4, query_glass_4))