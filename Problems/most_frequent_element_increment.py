def maxFrequency(nums, k):
        left=0
        max_freq=0
        total=0

        for right in range(len(nums)):
            total+=nums[right]

            while nums[right]*(right-left+1) - total > k:
                total-=nums[left]
                left+=1
            
            max_freq = max(max_freq,right-left+1)
        
        return max_freq

print(maxFrequency([1,2,4],5))