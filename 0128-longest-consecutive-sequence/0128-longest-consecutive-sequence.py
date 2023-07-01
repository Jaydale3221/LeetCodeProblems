class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        num_counts = collections.Counter(nums)  # Count the frequencies of numbers in the list
        max_sequence_length = 0  # Variable to store the length of the longest consecutive sequence

        for num in nums:
            if num - 1 not in num_counts:  # Check if the previous number is not in the list
                current_num = num  # Start a new sequence with the current number
                current_sequence_length = 1  # Initialize the length of the current sequence

                while current_num + 1 in num_counts:  # Continue the sequence by checking the next number
                    current_num += 1  # Increment the current number
                    current_sequence_length += 1  # Increment the length of the current sequence

                max_sequence_length = max(max_sequence_length, current_sequence_length)  # Update the maximum sequence length if necessary

        return max_sequence_length  # Return the length of the longest consecutive sequence
