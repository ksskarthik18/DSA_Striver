#Time Complexity  = O (log n+m) X O(n+m)

def swapGreater(nums1,nums2,left,right):
    if nums1[left]>nums2[right]:
        nums1[left],nums2[right] = nums2[right],nums1[left]

def merge_arrays(nums1,n,nums2,m):

    len = m + n
    gap = (len//2) + (len%2)
    while gap>0:
        left = 0
        right = left + gap
        while right < len:
            if left < n and right >= n:
                swapGreater(nums1,nums2,left,right-n)
            elif left >= n:
                swapGreater(nums1,nums2,left-n,right-n)
            else:
                swapGreater(nums1,nums2,left,right)
            left+=1
            right+=1
        if gap == 1:
            break
        gap = (gap//2) + (gap%2)

def main():
    nums1=[1,3,5,7]
    nums2=[5,6,7,8,9]
    merge_arrays(nums1,len(nums1),nums2,len(nums2))
    print(nums1 + nums2)

main()