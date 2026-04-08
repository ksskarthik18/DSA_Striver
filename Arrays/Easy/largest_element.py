def largest_element(arr):
    if not arr:
        return None
    
    max_element=arr[0]
    for i in range(len(arr)):
        if arr[i]>max_element:
            max_element=arr[i]
    
    return max_element

def main():
    arr=[6,1,4,9,8,2,3]
    print(largest_element(arr))
main()



