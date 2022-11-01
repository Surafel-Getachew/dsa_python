def longest_consecutive (nums):
#         check if current is has left if true procede
#         else check it has right if true check it's right has right and increment count
#         procede
    numSet = set(nums);
    longest = 0;
    for i in range(len(nums)):
        if nums[i] -1 not in numSet:
            right = nums[i] + 1
            rightCount = 1;
            while (right in numSet):
                rightCount +=1
                right +=1
            longest = max(longest,rightCount)
    return longest