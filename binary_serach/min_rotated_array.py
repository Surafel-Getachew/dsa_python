# 9,8,0,1,2,3,4,5

def min_rotated_sorted_array(nums):
    l, r = 0, len(nums) - 1
    res = max(nums)

    while l <= r:
        mid = (l+r) // 2
        res = min(res, nums[mid])

        if nums[mid] < nums[r]:
            r = mid - 1
        elif nums[mid] > nums[r]:
            l = mid + 1
        else:
            return res
    return res


nums = [3,1,2]
nums = [3, 4, 5, 1, 2]
print(min_rotated_sorted_array(nums))
