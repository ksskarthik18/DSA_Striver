#Time Complexity : log(min(n1,n2) base 2)
def kth_element_sorted_arrays(nums1,nums2,k):
    if len(nums2) < len(nums1) :
        return kth_element_sorted_arrays(nums2,nums1)
    n1= len(nums1)
    n2= len(nums2)
    low = max(0,k-n2)
    high = min(k,n1)
    while low <= high:
        cut1 = (low + high)//2
        cut2 = (n1+n2 +1)//2 - cut1

        left1 = float('-inf') if cut1 == 0 else nums1[cut1-1]
        left2 = float('-inf') if cut2 == 0 else nums2[cut2-1]

        right1 = float('inf') if cut1 == n1 else nums1[cut1]
        right2 = float('inf') if cut2 == n2 else nums2[cut2]

        if left1 <= right2 and left2 <= right1 :
                return max(left1,left2)
        
        elif left1 > right2:
            high = cut1 - 1
        else :
            low = cut1 + 1
    return 0

def main():
    nums1 = [2,3,45]
    nums2 = [4,6,7,8]
    k=4
    print(kth_element_sorted_arrays(nums1,nums2,k))

main()  
