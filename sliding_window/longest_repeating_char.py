from cmath import inf

def longest_repeating_char(s,k):
    count = {}
    res = 0;

    l = 0
    for r in range(len(s)):
        count[s[r]] = 1 + count.get(s[r],0)

        while (r - l +1) - max(count.values()) > k:
            count[s[l]] -= 1;
            l+=1
        
        res = max(res, r- l + 1)
    
    return res

    
s = "ABAB"
k = 2

print(longest_repeating_char(s,k))




# def longest_repeating_char(s,k):
#     changeLimit = k
#     i,j = 0,1
#     maxCount = 0;
#     count = 1;
#     nextI = inf;
#     while i < len(s):
#         while j<len(s):
#             if s[i] == s[j]:
#                 count+=1
#                 j+=1
                
#             elif s[i] != s[j] and changeLimit > 0:
#                 count+=1
#                 j+=1
#                 changeLimit -=1
#                 nextI = min(nextI,j)
#             else:
#                 i = nextI
#                 j = i+1;
#                 changeLimit = k
#                 maxCount = max(maxCount,count)
#                 count = 1
#                 break;
#     return maxCount
