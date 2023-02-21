from collections import deque


def find_max_sliding_window(nums, window_size):

    lista = []

    l = 0
    if window_size > len(nums):
        return nums
    for r in range(window_size - 1, len(nums)):
        if r - l > window_size - 1:
            l += 1
        m = l
        max_val = float("-inf")
        while m <= r:
            max_val = max(max_val, nums[m])
            m += 1
        lista.append(max_val)
    return lista


def find_max_sliding_window2(nums, window_size):
    window = deque()
    lista = []

    for i in range(window_size):
        while window and nums[i] >= nums[window[-1]]:
            window.popleft()
        window.append(i)

    lista.append(nums[window[0]])

    for i in range(window_size, len(nums)):
        if window[0] <= i - window_size:
            window.popleft()

        while window and nums[i] >= nums[window[-1]]:
            window.popleft()
        window.append(i)
        lista.append(nums[window[0]])

    return lista


nums = [10, 6, 9, -3, 23, -1, 34, 56, 67, -1, -4, -8, -2, 9, 10, 34, 67]
w = 2
print(find_max_sliding_window2(nums, w))


#  exp  [10, 9, 9, 23, 23, 34, 56, 67, 67, -1, -4, -2, 9, 10, 34, 67]
# act [10, 9, 9, 23, 23, 34, 56, 67, 67, 0, 0, 0, 9, 10, 34, 67]
