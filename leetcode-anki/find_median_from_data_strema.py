from heapq import *


class MedianFinder(object):
    def __init__(self) -> None:
        self.small_elem_maxH = []
        self.large_elem_minH = []

    def addNum(self, num):
        if self.small_elem_maxH and num <= -self.small_elem_maxH[0]:
            heappush(self.small_elem_maxH, -num)
        else:
            heappush(self.large_elem_minH, num)

        # rebalancing
        if len(self.large_elem_minH) > len(self.small_elem_maxH) + 1:
            heappush(self.small_elem_maxH, -heappop(self.large_elem_minH))
        elif len(self.large_elem_minH) < len(self.small_elem_maxH):
            heappush(self.large_elem_minH, -heappop(self.small_elem_maxH))

    def findMedian(self):
        if len(self.small_elem_maxH) != len(self.large_elem_minH):
            return self.large_elem_minH[0] / 1.0
        else:
            return -self.small_elem_maxH[0] / 2.0 + self.large_elem_minH[0] / 2.0


obj = MedianFinder()
obj.addNum(-1)

print(obj.findMedian())
obj.addNum(-2)

print(obj.findMedian())
obj.addNum(-3)
print(obj.findMedian())
obj.addNum(-4)

print(obj.findMedian())
obj.addNum(-5)
print(obj.findMedian())
# obj.insert_num(27)
# print(obj.find_median())
