class Solution:
    def maximumUniqueSubarray(self, nums: List[int]) -> int:
        counts = collections.Counter()
        current = answer = left = 0

        for right in range(len(nums)):
            current += nums[right]

            counts[nums[right]] += 1

            while counts[nums[right]] > 1:
                current -= nums[left]
                counts[nums[left]] -= 1
                left += 1
            
            answer = max(current,answer)
        
        return answer


