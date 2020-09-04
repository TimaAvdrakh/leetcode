def thousandSeparator(n):
    ans = ""
    for ix, num in enumerate(reversed(str(n)),1):
        ans += num

        if ix % 3 == 0 and ix < len(str(n)):
            ans += '.'
    return "".join(list(reversed(ans)))