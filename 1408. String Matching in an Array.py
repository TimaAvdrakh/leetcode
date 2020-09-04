def stringMatching(words):

    unique = set()

    for word1 in words:
        for word2 in words:
            if word1 in word2 and word1 != word2:
                unique.add(word1)
    return unique