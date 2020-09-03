def to_lower_case(str):
    ans = ""
    lt = list(str)
    for i in lt:
        if ord(i) > 64 and ord(i) < 91:
            ans += chr(ord(i)+32)
        else:
            ans += i
    return ans

print(to_lower_case("SasdaSdasd"))