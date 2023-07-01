class Solution:
    def maximumUniqueSubarray(self, nums: List[int]) -> int:
        num_counts = collections.Counter()  # Counter to track the frequencies of numbers
        max_sum = left = current_sum = 0  # Variables for maximum sum, left pointer, and current sum

        for right in range(len(nums)):
            current_sum += nums[right]  # Add the current number to the running sum

            num_counts[nums[right]] += 1  # Increment the count of the current number

            while num_counts[nums[right]] > 1:  # Adjust the window while the current number is not unique
                current_sum -= nums[left]  # Subtract the leftmost element from the current sum
                num_counts[nums[left]] -= 1  # Decrement the count of the leftmost element

                left += 1  # Move the left pointer to the right

            max_sum = max(current_sum, max_sum)  # Update the maximum sum if necessary

        return max_sum  # Return the maximum sum of a subarray with unique elements
