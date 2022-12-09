import math
def koko_bananas(piles, hr):
        l,r = 1,max(piles)
        res = r
        while l <= r:
            mid = (l + r) // 2
            hours = 0
            for p in piles:
                hours += math.ceil(p/mid)
            if hours <= h:
                res = min(res,mid)
                r = mid - 1
            else:
                
                l = mid + 1
        
        return res


# piles = [3, 6, 7, 11]
# h = 8

# piles = [30, 11, 23, 4, 20]
# h = 5

# piles = [312884470]
# h = 312884469
piles = [4]
h = 3

print(koko_bananas(piles, h))
