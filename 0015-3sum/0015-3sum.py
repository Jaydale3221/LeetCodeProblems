class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]: 
        nums.sort() # sorting cause we need to avoid duplicates, with this duplicates will be near to each other
        l=[]

        for i in range(len(nums)):   
            if i>0 and nums[i-1]==nums[i]:  #skipping if we found the duplicate of i
                continue 
            # Two pointer approach below
            j = i + 1 
            k = len(nums)-1 
            while j < k: 
                s=nums[i]+nums[j]+nums[k] 
                if s > 0: 
                    k -= 1  
                elif s < 0: 
                    j += 1  
                else:
                    l.append([nums[i],nums[j],nums[k]]) #if sum s found equal to the target (0)
                    j += 1 
                    # don't need duplicates to calculate so
                    while nums[j-1]==nums[j] and j<k: #skipping if we found the duplicate of j
                        j+=1   
        return l