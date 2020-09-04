def sortString(s):

    from collections import Counter
    ans = ""
    list_str = list(s)
    c = Counter(list_str)
    print(sorted(c.keys()))
    while c:
        for i in sorted(c.keys()):
            if c[i] > 0:
                ans += i
                c[i] -= 1
            else:
                del c[i]

        for i in sorted(c.keys(), reverse=True):
            if c[i] > 0 :
                ans += i
                c[i] -= 1
            else:
                del c[i]
    return ans
    
print(sortString("aaabbbccc"))
