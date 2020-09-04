def maxNumberOfBalloons( text):

    from collections import Counter

    c = Counter(text)

    for key in c.keys():
        if key not in 'balon':
            c.pop(key)
    c['l'] /= 2
    c['o'] /= 2

    if len(c)< 5:
        return 0
    return min(c.values())