class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        answer = []  # Initialize an empty list to store the maximum values.
        queue = deque()  # Initialize an empty deque to store indices.

        for i in range(len(nums)):  # Iterate through each element in the input list.
            while queue and nums[queue[-1]] < nums[i]:
                # While the queue is not empty and the last element in the queue has a smaller value than the current element.
                queue.pop()  # Remove the last element from the queue.
            
            queue.append(i)  # Add the current index to the queue.
            
            if queue[0] + k == i:
                # If the index at the front of the queue (which represents the maximum value) is outside the current sliding window.
                queue.popleft()  # Remove the front element from the queue.
            
            if i >= k - 1:
                # If the current index is greater than or equal to the window size (k - 1).
                answer.append(nums[queue[0]])  # Add the maximum value (at the front of the queue) to the answer list.
        
        return answer  # Return the list of maximum values in the sliding windows.
