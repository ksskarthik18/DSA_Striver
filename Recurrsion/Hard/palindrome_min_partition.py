#Time Compelexity : O(n) x n
def check_min_partition(word):
    n = len(word)

    def f(i):
        min_cost = float('inf')
        if i == n:
            return 0
        
        for j in range(i,n):
            if isPalindrome(i,j,word):
                cost = 1 + f(j+1)
                min_cost = min(min_cost,cost)

        return min_cost
    return f(0)-1 

        
    

def isPalindrome(i,j,word):
    while i<j:
        if word[i] != word[j]:
            return False
        i+=1
        j-=1

    return True

def main():
    word = "bababcbadcede"
    print(check_min_partition(word))
main()
    