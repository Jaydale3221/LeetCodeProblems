class Solution:
    def numSubarraysWithSum(self, nums: List[int], goal: int) -> int:
        addition = collections.Counter()
        addition[0] = 1
        answer = current = 0

        for num in nums:
            current += num

            if current - goal in addition:
                answer += addition[current - goal]

            addition[current] += 1

        return answer
