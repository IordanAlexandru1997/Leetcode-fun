from collections import Counter
from heapq import *


def reorganize_string(input_string):
    rez = ""
    d = {}
    for s in input_string:
        d[s] = 1 + d.get(s, 0)
    # print(d)
    # d = {k: v for k, v in sorted(d.items(), key=lambda item: item[1], reverse=True)}
    max_heap = []
    prev = None
    for k, v in d.items():
        heappush(max_heap, (-v, k))
    while max_heap or prev:

        if prev and len(max_heap) == 0:
            return ""

        v, k = heappop(max_heap)
        rez += k
        v += 1

        if prev:
            heappush(max_heap, prev)
            prev = None
        if v != 0:
            prev = (v, k)
    return rez


s = "aaabc"
print(reorganize_string(s))
