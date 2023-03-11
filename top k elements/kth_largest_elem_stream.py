from heapq import *

# Tip: You may use some of the code templates provided
# in the support files


class KthLargest:
    # constructor to initialize heap and add values in it
    # constructor to initialize heap and add values in it
    def __init__(self, k, nums):
        self.min_h = nums
        heapify(self.min_h)
        while len(self.min_h) > k:
            heappop(self.min_h)

    # adds element in the heap
    def add(self, val):
        if self.min_h and self.min_h[0] <= val:
            heappop(self.min_h)
            heappush(self.min_h, val)
        elif not self.min_h or len(self.min_h) < self.k:
            heappush(self.min_h, val)
        return self.return_Kth_largest()

    # returns kth largest element from heap
    def return_Kth_largest(self):
        return self.min_h[0]


obj = KthLargest(3, [5, -1])
obj.add(2)
obj.add(1)
obj.add(-1)
obj.add(3)
print(obj.add(4))
