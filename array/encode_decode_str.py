def encode(strs):
    res = ""
    for s in strs:
        res += str(len(s)) + "#" + s;
    return res;

# def decode(strs):


strs = ["Hello","World","!"]

print(encode(strs))

s = "3#lon2#ab"
lst = []

print(s.split("#"))
    