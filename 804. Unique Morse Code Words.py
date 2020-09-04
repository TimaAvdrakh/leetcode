def uniqueMorseRepresentations(words):
    morse_list = [".-", "-...", "-.-.", "-..", ".", "..-.", "--.",
                  "....", "..", ".---", "-.-", ".-..", "--", "-.",
                  "---", ".--.", "--.-", ".-.", "...", "-", "..-",
                  "...-", ".--", "-..-", "-.--", "--.."]
    myset = set()
    for word in words:
        code = ""
        for letter in word:
            code += morse_list[ord(letter)-97]
        myset.add(code)
    return len(myset)