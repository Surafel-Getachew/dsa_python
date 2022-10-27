def is_subSequence (t,s):
    # abcde  ace
    # abcdec  aec

    i,j = 0,0

    while i < len(s) and j < len(t):
        if s[i] == t[j]:
            i+=1
        j+=1
    return True if i == len(s) else False


    # second solution
    for i in range(len(s)):
        if s[i] not in t:
            return False
        else:
            currentIndex = t.index(s[i]) # this has the time complexity of o(n)
            t = t[currentIndex+1:]
    return True


t="abcd"
s="ace"




print(is_subSequence(t,s))

