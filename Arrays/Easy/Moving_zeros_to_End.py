def move_zeros(arr):
    n=len(arr)

    j=-1
    for i in range(n):
        if arr[i]==0:
            j=i
            break
    if j == -1:
        return arr
    for i in range(j+1,n,1):
        if arr[i]!=0:
            arr[i],arr[j]=arr[j],arr[i]
            j+=1
    
    return arr

def main():
    arr=[1,0,2,0,3,0,4,5]
    print(move_zeros(arr))
main()
        
