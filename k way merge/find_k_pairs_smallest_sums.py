from heapq import *


def k_smallest_pairs(list1, list2, k):
    result = []
    min_sum_heap = []
    for i in range(min(k, len(list1))):
        heappush(min_sum_heap, (list1[i] + list2[0], i, 0))
    while k > 0 and min_sum_heap:
        _, i, j = heappop(min_sum_heap)
        result.append((list1[i], list2[j]))
        if j + 1 < len(list2):
            heappush(min_sum_heap, (list1[i] + list2[j + 1], i, j + 1))
        k -= 1
    return result


k = 10
l1 = [1, 1, 2]
l2 = [1, 2, 3]
# l1 = [1, 7, 11]
# l2 = [2, 4, 6]
print(k_smallest_pairs(l1, l2, k))
