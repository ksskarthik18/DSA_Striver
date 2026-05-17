def palindrome_partition(word):
    n = len(word)
    result = []

    def isPalindrome(i,j):
        while i<j:
            if word[i] != word[j]:
                return False
            i+=1
            j-=1
        return True
    
    result = []
    def backTrack(i,ds):
        if i == n:
            result.append(ds[:])
            return
        
        for j in range(i,n):
            if isPalindrome(i,j):
                ds.append(word[i:j+1])
                backTrack(j+1,ds)
                ds.pop()
    backTrack(0,[])
    return result

def main():
    word = "aabaa"
    print(palindrome_partition(word))
main()
                        




