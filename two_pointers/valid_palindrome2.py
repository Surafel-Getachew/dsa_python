from turtle import right


def valid_palindrome2(s):

    l,r = 0,len(s)-1;
    while (l < r ):
        if s[l].lower() != s[r].lower():
            skipL,skipR = s[l+1:r+1],s[l:r]
            return skipL == skipL[::-1] or skipR == skipR[::-1]
        l+=1    
        r-=1
    return True;


# s = "aba"
s = "abca"
# s = "abc"
# s="qmgmlcupuufxxfuupuculmgmq"

print(valid_palindrome2(s))