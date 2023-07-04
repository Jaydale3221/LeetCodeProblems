class Solution:
    def maximumSum(self, nums: List[int]) -> int:
         #get digit Sum
        def get_digit_sum(num):
            digitSum = 0

            while num:
                digitSum += num % 10
                num //= 10
            return digitSum

        #Use hash on digitsum to get which values have same digitsum

        store = defaultdict(list)
        for num in nums:
            _sum = get_digit_sum(num)
            store[_sum].append(num)
        
        answer = -1
        for key in store:
            current = store[key]
            # print(key)

            if len(current) > 1:
                current.sort(reverse= True)
                answer = max(answer, current[0] + current[1])
            
        return answer
 
