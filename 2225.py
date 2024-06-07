# 2225. Find Players With Zero or One Losses
# https://leetcode.com/problems/find-players-with-zero-or-one-losses/

from typing import List
from typing import defaultdict

class Solution:

    def findWinners(self, matches: List[List[int]]) -> List[List[int]]:

        players_losses_counts = defaultdict(int)

        for winner, looser in matches:
            if winner not in players_losses_counts.keys():
                players_losses_counts[winner] = 0
            players_losses_counts[looser] += 1

        winners = sorted([u_id for u_id,l in players_losses_counts.items() if l == 0])
        one_losses = sorted([u_id for u_id,l in players_losses_counts.items() if l == 1])

        return [winners, one_losses]



matches_1 = [[1,3],[2,3],[3,6],[5,6],[5,7],[4,5],[4,8],[4,9],[10,4],[10,9]]
# Output: [[1,2,10],[4,5,7,8]]
# Explanation:
# Players 1, 2, and 10 have not lost any matches.
# Players 4, 5, 7, and 8 each have lost one match.
# Players 3, 6, and 9 each have lost two matches.
# Thus, answer[0] = [1,2,10] and answer[1] = [4,5,7,8].

matches_2 = [[2,3],[1,3],[5,4],[6,4]]
# Output: [[1,2,5,6],[]]
# Explanation:
# Players 1, 2, 5, and 6 have not lost any matches.
# Players 3 and 4 each have lost two matches.
# Thus, answer[0] = [1,2,5,6] and answer[1] = [].

