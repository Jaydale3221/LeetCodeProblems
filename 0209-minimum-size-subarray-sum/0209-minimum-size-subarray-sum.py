class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        left = current = 0
        answer = float('inf')

        for right in range(len(nums)):
            current += nums[right]

            while current >= target:
                current -= nums[left]
                answer = min(answer, right - left + 1)
                left += 1
            
            
        return answer if answer!= float('inf') else 0

       