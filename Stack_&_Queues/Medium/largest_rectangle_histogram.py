#Time Complexity :O(N) 
def largestRectangeHeights(heights):
    n = len(heights)
    stack = []
    maxArea = 0

    for i in range(n):
        while len(stack)!=0 and heights[stack[-1]] > heights[i]:
            element = stack[-1]
            stack.pop()
            nse = i
            if len(stack) == 0:
                pse = -1
            else:
                pse = stack[-1]
            maxArea = max(maxArea,heights[element]*(nse-pse-1))
        stack.append(i)
    while len(stack)!=0:
        nse = n
        element = stack[-1]
        stack.pop()
        pse = -1 if len(stack)==0 else stack[-1]
        maxArea = max(maxArea,heights[element]*(nse-pse-1))
    return maxArea


def main():
    heights = [2,1,5,6,2,3]
    print(largestRectangeHeights(heights))
main()