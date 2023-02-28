from heapq import *


class MedianOfStream:
    small_elem_maxH = []
    large_elem_minH = []
    # This function should take a number and store it
    def addNum(self, num):
        if not self.small_elem_maxH or num <= -self.small_elem_maxH[0]:
            heappush(self.small_elem_maxH, -num)
        else:
            heappush(self.large_elem_minH, num)

        if len(self.small_elem_maxH) > len(self.large_elem_minH) + 1:
            heappush(self.large_elem_minH, -heappop(self.small_elem_maxH))
        elif len(self.small_elem_maxH) < len(self.large_elem_minH):
            heappush(self.small_elem_maxH, -heappop(self.large_elem_minH))

    # This function should return the median of the stored numbers
    def findMedian(self):
        if len(self.small_elem_maxH) == len(self.large_elem_minH):
            return -self.small_elem_maxH[0] / 2.0 + self.large_elem_minH[0] / 2.0
        else:
            return -self.small_elem_maxH[0] / 1.0


obj = MedianOfStream()
obj.addNum(1)
print(obj.findMedian())
# obj.insert_num(35)
# obj.insert_num(36)
# print(obj.find_median())
# obj.insert_num(27)
# print(obj.find_median())
