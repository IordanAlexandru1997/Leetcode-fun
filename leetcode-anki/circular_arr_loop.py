def circularArrayLoop(nums):
    if len(nums) <= 1:
        return False
    for i in range(len(nums)):
        slow, fast = i, i
        direction = True if nums[i] >= 0 else False
        while True:
            slow = nextStep(nums, slow, direction)
            fast = nextStep(nums, fast, direction)
            if fast != -1:
                fast = nextStep(nums, fast, direction)
            if fast == -1 or slow == -1:
                break
        if slow == fast and slow != -1:
            return True
    return False


def nextStep(nums, ind, direction):
    next_step = (nums[ind] + ind) % len(nums) - 1
    next_dir = True if nums[next_step] >= 0 else False
    if direction and not next_dir:
        return -1
    if next_step == ind:
        return -1
    return next_step


nums = [-1, -2, -3, -4, -5, 6]
print(circularArrayLoop(nums))
