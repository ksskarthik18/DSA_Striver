#Time Complexity : O(N x L x 26)
# N = number of words in wordList
# L = length of each word
# 26 = number of lowercase letters

from collections import deque
def ladderLength(beginWord,endWord,wordList):
    wordSet = set(wordList)
    if endWord not in wordSet:
        return 0
    queue = deque()
    queue.append((beginWord,1))

    while queue:
        word,steps = queue.popleft()

        for i in range(len(word)):

            for ch in "abcdefghijklmnopqrstuvwxyz":
                new_word = word[:i] + ch + word[i+1:]

                if new_word == endWord:
                    return steps + 1
                if new_word in wordSet:
                    wordSet.remove(new_word)
                    queue.append((new_word,steps+1))

    return 0

beginWord = "hit" 
endWord = "cog"
wordList = ["hot","dot","dog","lot","log","cog"]
print(ladderLength(beginWord,endWord,wordList))

    