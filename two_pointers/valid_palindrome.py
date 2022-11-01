def valid_palindrome(s):

    l,r = 0,len(s) -1

    while(l < r):
        while l < r and not isAlphaNum(s[l]):
            l+=1
        while r > l and not isAlphaNum(s[r]):
            r-=1
        if s[l].lower() != s[r].lower():
            return False
        l,r = l + 1, r - 1
    
    return True

    s = "".join(letter for letter in s if letter.isalnum())
    s = s.lower()

    i, j = 0, len(s) - 1

    while (i < j):
        if s[i] == s[j]:
            i += 1
            j -= 1
        else:
            return False
    return True

# ord return the ascii value


def isAlphaNum(c):
    return ((ord("A") <= ord(c) <= ord("Z")) or
            (ord("a") <= ord(c) <= ord("z")) or
            (ord("0") <= ord(c) <= ord("9")))


s = "A man, a plan, a canal: Panama"
# s = "race a car"
# s="0P"

print(valid_palindrome(s))
