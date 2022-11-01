from math import inf
def sub_array_sum(nums,k):
    res =  0;
    sum = 0;
    prefixSums = {0:1}

    for num in nums:
        sum += num
        diff = sum - k
        
        res += prefixSums.get(diff,0)
        prefixSums[sum] = 1 + prefixSums.get(sum,0)

    return res;


nums = [1,-1,0] 
k=0

print(sub_array_sum(nums,k));

