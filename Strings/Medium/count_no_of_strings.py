#Time Complexity : O(n)
def count_no_of_strings(s,k):
    left = 0
    count = {}

    for right in range(len(s)):
        count[s[right]] = count.get(s[right],0)+1
