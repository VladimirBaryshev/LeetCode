# 2491. Divide Players Into Teams of Equal Skill
# https://leetcode.com/problems/divide-players-into-teams-of-equal-skill/description/

class Solution:

    def mult(self, a,b):
        return a*b

    def dividePlayers(self, skill: List[int]) -> int:
        pairs = []
        skill.sort()
        l_prev, r_prev = skill[0], skill[-1]
        while len(skill) != 0:
            l,r = skill.pop(0), skill.pop(-1)
            if sum((l_prev, r_prev)) != sum((l,r)):
                return -1
            pairs.append((l,r))
            l_prev, r_prev = l,r

        return sum((self.mult(*i) for i in pairs))

        