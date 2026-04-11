def intersection_array(nums1,nums2):
    n1=len(nums1)
    n2=len(nums2)
    i=0
    j=0

    intersection_array=[]
    while i<n1 and j<n2:
        if nums1[i]<nums2[j]:
            i+=1
        elif nums1[i]==nums2[j]:
            intersection_array.append(nums1[i])
            i+=1
            j+=1
        else :
            j+=1
    
    return intersection_array

def main():
    nums1= [1,2,2,3,4,5,6,7]
    nums2= [2,2,5,7,9]
    print(intersection_array(nums1,nums2))
main()
