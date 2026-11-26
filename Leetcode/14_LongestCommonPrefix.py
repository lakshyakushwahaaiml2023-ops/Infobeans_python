def prefix_strs(strs):
    prefix = strs[0]
    for i in strs:
        while not i.startswith(prefix):
            prefix = prefix[:-1]
        if prefix =="":
            return ""
    return prefix

strs = ["flower","flow","flight", "cat"]
print(prefix_strs(strs)) 