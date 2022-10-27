def common_prefix (strs):
    i,j,= 0,0
    commonPrefix=""
    # strs = ["flower","flow","flight"]
    for i in range(len(strs[0])):
        for s in strs:
            if i >= len(s) or strs[0][i] != s[i]:
                return commonPrefix;
        commonPrefix += s[i]
    return commonPrefix

    while j < len(strs[i]):
        while i < len(strs)-1:
            if j >= len(strs[i+1]):
                return commonPrefix
            elif strs[i][j] == strs[i+1][j]:
                i+=1
            else:
                return commonPrefix
        commonPrefix += strs[i][j]
        j+=1
        i=0;
    return commonPrefix

strs = ["flower","flow","flight"]
# strs = ["ab", "a"]



print(common_prefix(strs))