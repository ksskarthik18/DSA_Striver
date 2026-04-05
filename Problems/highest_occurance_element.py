def highest_occurance_element(arr):
    freq={}
    for num in arr:
        freq[num]= freq.get(num,0)+1
    
    max_count=0
    max_element=None

    for num in freq:
        if freq[num] > max_count:
            max_count = freq[num]
            max_element = num
    
    return max_element
arr = [1, 2, 2, 3, 1, 2]
print(highest_occurance_element(arr))
