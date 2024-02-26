# 743. Network Delay Time
# https://leetcode.com/problems/network-delay-time/description/


from typing import List
import collections, heapq


def networkDelayTime(times: List[List[int]], n: int, k: int) -> int:
    
    edges = collections.defaultdict(list)

    for u,v,w in times:
        edges[u].append([v,w])

    # print(edges)

    minHeap = [(0,k)]
    visit = set()
    t = 0

    while minHeap:
        w1, n1 = heapq.heappop(minHeap)
        if n1 in visit:
            continue
        visit.add(n1)
        t = w1

        for n2, w2 in edges[n1]:
            if n2 not in visit:
                    heapq.heappush(minHeap, (w1+w2, n2))

    if len(visit) == n:
        return t
    else:
        return -1


times_1 = [[2,1,1],[2,3,1],[3,4,1]]
n_1 = 4
k_1 = 2
# Output: 2

times_2 = [[1,2,1]]
n_2 = 2
k_2 = 1
# Output: 1

times_3 = [[1,2,1]]
n_3 = 2
k_3 = 2
# Output: -1

print(networkDelayTime(times_1, n_1, k_1))
print(networkDelayTime(times_2, n_2, k_2))
print(networkDelayTime(times_3, n_3, k_3))

