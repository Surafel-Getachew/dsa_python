def two_sum_2(nums,target):
    l,r = 0, len(nums) - 1
    while l < r:
        sum = nums[l] + nums[r]
        if sum > target:
            r-=1
        elif sum < target:
            l+=1
        else:
            return [l+1,r+1]
    return []
    for i in range(len(nums)):
        for j in range(i+1,len(nums),1):
            sum = nums[i] + nums [j]
            if sum == target:
                return [i+1,j+1]
            elif sum > target:
                break;
    return [];


numbers = [2,7,11,15] 
target = 9


print(two_sum_2(numbers,target))