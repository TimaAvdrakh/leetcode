def isPrefixWord(self, sentence, searchWord):

    li = searchWord.split(' ')

    for ind, word in enumerate(li):
        if searchWord == word[:len(searchWord)]:
           return ind
    return -1