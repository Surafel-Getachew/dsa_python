from cmath import inf

def min_window_subString(s,t):
    l,r = 0,len(s)
    res = inf
    t.sort()

    if len(t) > len(s):
        return ""
    
    while l < len(s):
        subStr = s[l:r].sort()
        print(res)
        if t in subStr:
            print(t)
            if len(subStr) < len(res):
                res = subStr
        
        l += 1
    
    return subStr

s = "ADOBECODEBANC" 
t = "ABC"

# print(min_window_subString(s,t))
# print("AB" in "CBBA".sort())

s = "CBBA"
ss = str(sorted(s))
print(ss)