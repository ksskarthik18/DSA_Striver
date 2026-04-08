def union_Array(arr1,arr2):
    n1=len(arr1)
    n2=len(arr2)
    i=0
    j=0
    union2=[]
    while i<n1 and j<n2:
        if arr1[i]<=arr2[j]:
            if not union2 or union2[-1]!=arr1[i]:
                union2.append(arr1[i])
            i+=1
        else:
            if not union2 or union2[-1]!=arr2[j]:
                union2.append(arr2[j])
            j+=1


    while i<n1:
        if  not union2 or union2[-1]!=arr1[i]:
                union2.append(arr1[i])
        i+=1

    while j<n2:
        if not union2 or union2[-1]!=arr2[j]:
                union2.append(arr2[j])
        j+=1

    return union2

def main():
     arr1=[1,2,3,4,5,6]
     arr2=[1,2,7,8]
     print(union_Array(arr1,arr2))
main()


