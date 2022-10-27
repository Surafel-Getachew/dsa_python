def length_of_last_word(s):
    i,length = len(s)-1,0
    while s[i] == " ":
        i-=1
    while i>=0 and s[i] != " ":
        length +=1
        i-=1
    return length

    count = 0
    for i in range(len(s)-1,-1,-1):
        if count==0 and s[i] == " ":
            continue;
        elif s[i] != " ":
            count+=1
        else:
            return count
    return count;

    # second solution

    # s = s.split(" ")
    # for i in range(len(s)-1,-1,-1):
    #     if "" != s[i]:
    #         return len(s[i])
    
# s = "Hello World "
# s = "   fly me   to   the moon  "
s="a"

print(length_of_last_word(s))