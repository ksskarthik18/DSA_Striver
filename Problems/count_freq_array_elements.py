def count_freq(arr):
    freq={}
    for num in arr:
        if num in freq:
            freq[num]+=1
        else:
            freq[num]=1
    
    return freq

arr=[1,2,2,3,1,4]
print(count_freq(arr))


# from collections import Counter
# freq=Counter(arr)
# print(freq)