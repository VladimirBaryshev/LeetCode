# 838. Push Dominoes

class Solution:

    def pushDominoes(self, dominoes: str) -> str:

        temp = ""
        
        while dominoes != temp:
            
            temp = dominoes
            dominoes = dominoes.replace("R.L", "xxx")
            dominoes = dominoes.replace("R.", "RR")
            dominoes = dominoes.replace(".L", "LL")

        # print(dominoes)

        return dominoes.replace("xxx", "R.L")

        
        




dominoes_1 = "RR.L"
# Output: "RR.L"
# Explanation: The first domino expends no additional force on the second domino.

dominoes_2 = ".L.R...LR..L.."
# Output: "LL.RR.LLRRLL.."

dominoes_3 = ".L.R.....LR..L.."
# Output: "LL.RRR.LLLRRLL.."

print(Solution().pushDominoes(dominoes_1))
print(Solution().pushDominoes(dominoes_2))
print(Solution().pushDominoes(dominoes_3))