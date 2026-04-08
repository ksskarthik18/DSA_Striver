def second_largest_element(arr):
    if len(arr) < 2:
        return None
    
    max_element=float('-inf')
    second_largest_element=float('-inf')
    for i in range(len(arr)):
        if arr[i]>max_element:
            second_largest_element= max_element
            max_element=arr[i]

        elif arr[i]>second_largest_element and arr[i]!=max_element:
            second_largest_element=arr[i]
    
    return second_largest_element if second_largest_element!= float('-inf') else None

def main():
    arr=[6,1,4,9,8,2,3]
    print(second_largest_element(arr))
main()