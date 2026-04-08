def left_rotate1(arr):
    n=len(arr)
    temp=arr[0]
    for i in range(1,n,1):
        arr[i-1]=arr[i]
    
    arr[n-1]=temp

    return arr

def main():
    arr=[1,2,3,4,5,6]
    print(left_rotate1(arr))
main()