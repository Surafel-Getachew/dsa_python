def two_sum(nums,target):
    prevMap = {}
    for i,n in enumerate(nums):
        diff = target - n;

        if diff in prevMap:
            return [i,prevMap[diff]]
        
        prevMap[n] = i;
        



nums = [2,7,11,15] 

print(two_sum(nums,9))