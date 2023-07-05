class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        stack = []
        map = defaultdict(lambda: -1)
        
        for num in nums2:
            while stack and num > stack[-1]:
                map[stack.pop()] = num
            stack.append(num)
        
        res = []
        for num in nums1:
            res.append(map[num])
        
        return res
