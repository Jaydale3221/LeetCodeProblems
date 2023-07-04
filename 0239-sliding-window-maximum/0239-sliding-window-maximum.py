class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        answer = []
        queue = deque()

        for i in range (len(nums)):
            while queue and nums[queue[-1]] < nums[i]:
                queue.pop()
            queue.append(i)

            if queue[0] + k == i:
                queue.popleft()
            
            if i >= k -1:
                answer.append(nums[queue[0]])
        return answer