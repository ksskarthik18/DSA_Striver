#Time Complexity : O(n)

def removeOuterParentheses(s):
    result = []
    depth = 0
    for ch in s:
        if ch == '(':
            if depth > 0:
                result.append('(')
            depth+=1
        else:
            depth-=1
            if depth>0:
                result.append(')')
    return "".join(result)

def main():
    s="(()())(())"
    print(removeOuterParentheses(s))
main()