def generate_parenthesis(n):
    result =[]

    def backTrack(current,openCount,closeCount):
        if len(current) == 2*n:
            result.append(current)
            return
        
        if openCount<n:
            backTrack(current + "(",openCount+1,closeCount)
        
        if closeCount < openCount:
            backTrack(current + ")",openCount,closeCount+1)
    backTrack("",0,0)

    return result

def main():
    print(generate_parenthesis(3))
main()
    
