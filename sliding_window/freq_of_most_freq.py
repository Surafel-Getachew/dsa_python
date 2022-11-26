def freq_of_most_freq (nums,k):
    nums.sort()

    l,r = 0,0
    res,total = 0,0

    while r < len(nums):
        total += nums[r]
        while nums[r] * (l-r+1) > total + k:
            total -= nums[l]
            l +=1
        
        res = max(res,r-l+1)
        r+=1
    return res

nums = [1,2,4]
k = 5
print(freq_of_most_freq(nums,k))