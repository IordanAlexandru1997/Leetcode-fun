# from collections import heapq
from heapq import *


def k_smallest_number(lists, k):
    min_heap = []
    for i in range(len(lists)):
        heappush(min_heap, (lists[i][0], i, 0))

    while min_heap and k > 1:
        val, l_idx, next_elem = heappop(min_heap)
        if next_elem + 1 < len(lists[l_idx]):
            heappush(min_heap, (lists[l_idx][next_elem + 1], l_idx, next_elem + 1))
        k -= 1
    if k == 1:
        return val
    if k > 1:
        return lists[l_idx][-1]
    return 0


lists = [[2, 6, 8], [3, 7, 10], [5, 8, 11]]
k = 5
print(k_smallest_number(lists, k))
