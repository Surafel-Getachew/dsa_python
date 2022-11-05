from cmath import inf


def min_difference(nums,k):
    res = float("inf")
    nums.sort();
    r,l = len(nums) -1, len(nums) - 1 - (k -1)
    while l >= 0:
        res = min(res,nums[r] - nums[l])
        l,r = l - 1, r - 1
    return res;

nums = [9,4,1,7];
k = 2


print(min_difference(nums,k))

