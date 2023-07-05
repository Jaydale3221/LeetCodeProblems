class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        stack = []
        answer = [0 for i in range(len(nums1))]
        counts = collections.Counter()
        
        for num in nums2:
            while stack and stack[-1] < num:
                counts[stack.pop()] = num
            stack.append(num)
            
        while stack:
            counts[stack.pop()] = -1
        
        print(counts)
        for i in range(len(nums1)):
            answer[i] = counts[nums1[i]]
        return answer
            
            
        