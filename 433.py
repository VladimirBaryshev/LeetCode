# 433. Minimum Genetic Mutation
# https://leetcode.com/problems/minimum-genetic-mutation/description/


from typing import List


class Solution:

    def minMutation(self, startGene: str, endGene: str, bank: List[str]) -> int:

        bank = set(bank)
        options = ['A', 'C', 'G', 'T']
        visited = set(startGene)
        queue = [startGene]
        count = 0

        while queue:

            for i in range(len(queue)):
                curGene = queue.pop(0)
                if curGene == endGene:
                    return count

                for option in options:
                    for i in range(8):

                        newGene = curGene[:i] + option + curGene[i+1:]
                        
                        if newGene in bank and newGene not in visited:
                            queue.append(newGene)
                            visited.add(newGene)
            count += 1

        return -1



startGene_1 = "AACCGGTT"
endGene_1 = "AACCGGTA"
bank_1 = ["AACCGGTA"]
# Output: 1

startGene_2 = "AACCGGTT"
endGene_2 = "AAACGGTA"
bank_2 = ["AACCGGTA","AACCGCTA","AAACGGTA"]
# Output: 2

startGene_3 = "AACCGGTT"
endGene_3 = "AACCGCTA"
bank_3 = ["AACCGGTA","AACCGCTA","AAACGGTA"]
# Output: 2

print(Solution().minMutation(startGene_1, endGene_1, bank_1))
print(Solution().minMutation(startGene_2, endGene_2, bank_2))
print(Solution().minMutation(startGene_3, endGene_3, bank_3))










