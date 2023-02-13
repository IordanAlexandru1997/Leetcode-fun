def find_sum_of_three(nums, target):
    nums.sort()

    suma = 0
    for i in range(len(nums) - 1):
        low = i + 1
        high = len(nums) - 1
        suma = nums[i] + nums[low] + nums[high]
        while suma != target and low != high:
            suma = nums[i] + nums[low] + nums[high]
            if suma < target:
                low += 1
            else:
                high -= 1
        if suma == target:
            return True
    return False


target = 10
nums = [3, 7, 1, 2, 8, 4, 5]
target = -1
nums = [-1, 1, 0]
print(find_sum_of_three(nums, target))
