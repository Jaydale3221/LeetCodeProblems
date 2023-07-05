class Solution:
    def longestSubarray(self, nums: List[int], limit: int) -> int:
        increasing = deque()  # Deque to store elements in increasing order.
        decreasing = deque()  # Deque to store elements in decreasing order.
        left = ans = 0  # Initialize variables for the left pointer and the answer.

        for right in range(len(nums)):  # Iterate through each element using the right pointer.
            # Maintain the monotonic deques for increasing and decreasing order.
            while increasing and increasing[-1] > nums[right]:
                # While the increasing deque is not empty and the last element is greater than the current element.
                increasing.pop()  # Remove the last element from the increasing deque.
            while decreasing and decreasing[-1] < nums[right]:
                # While the decreasing deque is not empty and the last element is smaller than the current element.
                decreasing.pop()  # Remove the last element from the decreasing deque.
                
            increasing.append(nums[right])  # Add the current element to the increasing deque.
            decreasing.append(nums[right])  # Add the current element to the decreasing deque.
            
            # Maintain the window property where the difference between the maximum and minimum elements is within the limit.
            while decreasing[0] - increasing[0] > limit:
                # While the difference between the first elements of decreasing and increasing deques is greater than the limit.
                if nums[left] == decreasing[0]:
                    # If the leftmost element in the window is equal to the first element of the decreasing deque.
                    decreasing.popleft()  # Remove the leftmost element from the decreasing deque.
                if nums[left] == increasing[0]:
                    # If the leftmost element in the window is equal to the first element of the increasing deque.
                    increasing.popleft()  # Remove the leftmost element from the increasing deque.
                left += 1  # Move the left pointer to the right to shrink the window.
            
            ans = max(ans, right - left + 1)  # Update the answer by taking the maximum length of the valid subarray.

        return ans  # Return the maximum length of the subarray satisfying the given limit.
