def check_array(arr):
    n=len(arr)
    count=0

    for i in range(n):
        if arr[i] > arr[(i+1)%n] :
            count+=1
    
    return count <= 1

def main():
    nums=[3,4,5,1,2]
    #nums=[2,1,3,4]
    print(check_array(nums))
main()