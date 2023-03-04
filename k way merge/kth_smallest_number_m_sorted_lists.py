from heapq import *

# works bcoz asc
def k_smallest_number(lists, k):
    min_heap = []
    max_len = 0
    for i in range(len(lists)):
        if not lists[i]:
            continue
        heappush(min_heap, (lists[i][0], i, 0))
        max_len = max(max_len, len(lists[i]))
    if not min_heap:
        return 0
    while len(min_heap) >= 1 and k > 1:
        val, idx, li = heappop(min_heap)
        if not min_heap and k > max_len:
            return lists[idx][-1]
        li += 1
        if li == len(lists[idx]):
            continue
        heappush(min_heap, (lists[idx][li], idx, li))
        k -= 1
    if k == 1:
        return min_heap[0][0]
    return 0


lists = [[4, 90, 1], [3, 100], [8, 9]]
k = 50
print(k_smallest_number(lists, k))

# min_heap = []
# for i in range(len(lists)):
#     if not lists[i]:
#         continue
#     heappush(min_heap, (lists[i][0], i, 0))
# while k > 0 and min_heap:
#     val, idx, li = heappop(min_heap)
#     if li + 1 < len(lists[idx]):
#         heappush(min_heap, (lists[idx][li + 1], idx, li + 1))
#     k -= 1
# if k > 0:
#     return 0
# return val
