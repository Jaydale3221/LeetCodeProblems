class Solution:
    def mostCompetitive(self, nums: List[int], k: int) -> List[int]:
        chances = len(nums) - k
        sequence = collections.deque()


        for num in nums:
            while sequence and sequence[-1] > num and chances != 0:
                sequence.pop()
                chances -= 1
            sequence.append(num)
            
        # print(k)
        return list(sequence)[:k]

        