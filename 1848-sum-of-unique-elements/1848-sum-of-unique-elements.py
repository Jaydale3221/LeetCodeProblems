class Solution:
    def sumOfUnique(self, nums: List[int]) -> int:
        # Use Counter to count the occurrences of each number
        counts = collections.Counter(nums)
        addition = 0

        # Iterate through the counts
        for count in counts:
            # Add the number to addition if its count is equal to 1
            if counts[count] == 1:
                addition += count
            
        return addition
