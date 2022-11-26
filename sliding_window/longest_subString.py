def length_longest_sub_string(s):
    charS = set()
    l = 0;
    res = 0;

    for r in range(len(s)):
        while s[r] in charS:
            charS.remove(s[l])
            l+=1
        charS.add(s[r])
        res = max(res,r-l+1)    
    
    return res

    
    if len(s) <= 0:
            return 0
        
    myStr = "" + s[0] 
    l,r = 0,1
    res = 1
    
    while (l<len(s) and r < len(s)):
        if s[r] not in myStr:
            myStr = myStr + s[r]
            res = max(res,len(myStr))
            r+=1
        else:
            res = max(res,len(myStr))
            l += 1
            r = l + 1
            myStr= "" + s[l]
    return res