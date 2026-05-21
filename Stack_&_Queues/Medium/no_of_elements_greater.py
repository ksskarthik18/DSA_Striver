def greater_elements_right(arr,indices):
    n = len(arr)
    result=[]
    for idx in indices:
        count = 0
        for j in range(idx+1,len(arr)):
            if arr[j]>arr[idx]:
                count+=1
        
        result.append(count)
    return result

def main():

    arr = [3,4,2,7,5,8,10,6]
    indices = [0,5]

    print(greater_elements_right(arr, indices))

main()