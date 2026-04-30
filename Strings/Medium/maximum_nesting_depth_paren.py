#Time Complexity : O(n)
def find_max_depth(s) :
    depth = 0
    max_depth=0
    for ch in s:
        if ch == '(':
            depth+=1
            max_depth = max(depth,max_depth)
        elif ch == ')':
            depth -= 1
    return max_depth

def main():
    s="(1)+((2))+(((3)))"
    print(find_max_depth(s))
main()