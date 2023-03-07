from heapq import *


def kth_smallest_element(matrix, k):
    min_heap = []
    for i in matrix:
        heappush(min_heap, (i[0], i, 0))
    while min_heap and k > 0:
        val, row, j = heappop(min_heap)
        if j + 1 < len(row):
            heappush(min_heap, (row[j + 1], row, j + 1))
        k -= 1
    if k >= 0:
        return val


matrix = [
    [1, 3, 5, 7, 9],
    [2, 4, 6, 8, 10],
    [11, 13, 15, 17, 19],
    [12, 14, 16, 18, 20],
    [21, 22, 23, 24, 25],
]
k = 11
print(kth_smallest_element(matrix, k))
