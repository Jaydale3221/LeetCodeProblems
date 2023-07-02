class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        chars = Counter()

        left = right = 0

        res = 0
        while right < len(s):
            r = s[right]
            chars[r] += 1

            while chars[r] > 1:
                l = s[left]
                chars[l] -= 1
                left += 1

            res = max(res, right - left + 1)

            right += 1
        return res
        # seen = collections.Counter()
        # left = answer = 0
        # for right in range(len(s)):
        #     seen[s[right]] += 1
        #     while seen[s[right]] > 1:
        #         seen[s[left]] -= 1
        #         left += 1    
        #     answer = max(answer, right-left+1)
        # return answer


        # seen = {}
        # left = answer = count =  0 
        
        # for right in range(len(s)):
        #     seen.append(right)
        #     count += 1

        #     while seen[s[right]] > 1:
        #         count -= 1
        #         left += 1
        #     answer = max(answer, right -left + 1 )

        # return answer  
        
