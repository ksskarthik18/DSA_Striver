def word_break(s,wordDict):
    words = set(wordDict)
    memo ={}

    def backTrack(index):
        if index == len(s):
            return True
        
        if index in memo:
            return memo[index]
        
        for j in range(index,len(s)):
            word = s[index:j+1]
            if word in words:
                if backTrack(j+1):
                    memo[index] = True
                    return True
        
        memo[index] = False
        return False
    return backTrack(0)

def main():

    s = "takeuforward"
    wordDict = ["take","forward","you","u"]

    print(word_break(s,wordDict))

main()