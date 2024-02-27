# 787. Cheapest Flights Within K Stops
# https://leetcode.com/problems/cheapest-flights-within-k-stops/description/


from typing import List


def findCheapestPrice(n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:

    prices = [float("inf")] * n
    prices[src] = 0

    for i in range(k+1):
        tmp_prices = prices.copy()

        for s,d,p in flights:
            # print(s,d,p)
            if prices[s] == float("inf"):
                continue
            if prices[s]+p < tmp_prices[d]:
                tmp_prices[d] = prices[s] + p

            # print(tmp_prices)

        prices = tmp_prices

    if prices[dst] == float("inf"):
        return -1
    else:
        return  prices[dst]



n_1 = 4
flights_1 = [[0,1,100],[1,2,100],[2,0,100],[1,3,600],[2,3,200]]
src_1 = 0
dst_1 = 3
k_1 = 1
# Output: 700
# Explanation:
# The optimal path with at most 1 stop from city 0 to 3 is marked in red and has cost 100 + 600 = 700.
# Note that the path through cities [0,1,2,3] is cheaper but is invalid because it uses 2 stops.


n_2 = 3
flights_2 = [[0,1,100],[1,2,100],[0,2,500]]
src_2 = 0
dst_2 = 2
k_2 = 1
# Output: 200
# Explanation:
# The graph is shown above.
# The optimal path with at most 1 stop from city 0 to 2 is marked in red and has cost 100 + 100 = 200.

n_3 = 3
flights_3 = [[0,1,100],[1,2,100],[0,2,500]]
src_3 = 0
dst_3 = 2
k_3 = 0
# Output: 500
# Explanation:
# The graph is shown above.
# The optimal path with no stops from city 0 to 2 is marked in red and has cost 500.


print(findCheapestPrice(n_1, flights_1, src_1, dst_1, k_1))
print(findCheapestPrice(n_1, flights_2, src_2, dst_2, k_2))
print(findCheapestPrice(n_1, flights_3, src_3, dst_3, k_3))




