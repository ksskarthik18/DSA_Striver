def left_rotate_kplaces(arr,k):
    n=len(arr)
    k=k%n

    def reverse_array(start,end):
        while start < end:
            arr[start],arr[end]=arr[end],arr[start]
            start+=1
            end-=1
        
    
    reverse_array(0,k-1)
    reverse_array(k,n-1)
    reverse_array(0,n-1)

    return arr

def main():
    arr=[1,2,3,4,5,6,7]
    k=3
    print(left_rotate_kplaces(arr,k))
main()


