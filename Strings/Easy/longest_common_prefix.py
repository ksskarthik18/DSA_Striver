#Time Complexity : O(n*m)
def find_longest_common_prefix(strs):
    if not strs:
        return ""
    for i in range(len(strs[0])):
        char = strs[0][i]
        for s in strs:
            if i >= len(strs) or s[i] != char:
                return strs[0][:i]
    return strs[0]
    

def main():
    strs = ["flower","flow","flight"]
    print(find_longest_common_prefix(strs))
main()
