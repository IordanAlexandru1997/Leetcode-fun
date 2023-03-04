def threeSum(nums):
    nums.sort()
    s = set()
    for i in range(len(nums) - 1):
        if i > 0 and nums[i] == nums[i - 1]:
            continue
        start = i + 1
        end = len(nums) - 1
        suma = nums[i] + nums[start] + nums[end]
        while start < end:
            suma = nums[i] + nums[start] + nums[end]
            if suma > 0:
                end -= 1
            elif suma < 0:
                start += 1
            if suma == 0:
                s.add((nums[i], nums[start], nums[end]))
                start += 1
                end -= 1
    lista = [list(x) for x in s]
    return lista

    # nums.sort()
    # s = []

    # end = len(nums) - 1
    # for i in range(len(nums) - 1):
    #     if i > 0 and nums[i] == nums[i - 1]:
    #         continue
    #     start = i + 1
    #     end = len(nums) - 1
    #     while start < end:
    #         suma = nums[i] + nums[start] + nums[end]
    #         if suma == 0:
    #             s.append([nums[start], nums[i], nums[end]])
    #             start += 1
    #             end -= 1
    #             while nums[start - 1] == nums[start]:
    #                 start += 1
    #             while nums[end + 1] == nums[end]:
    #                 end -= 1
    #         elif suma > 0:
    #             end -= 1
    #         else:
    #             start += 1
    # return s


nums = [-1, 0, 1, 2, -1, -4, -2, -3, 3, 0, 4]
print(threeSum(nums))
