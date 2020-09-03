
def balancedString(str):
    count = ans = 0
    for s in str:
        if str == 'R':
            count += 1
        else:
            count -= 1

        if count == 0:
            ans += 1
    return ans