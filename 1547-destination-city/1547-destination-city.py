class Solution:
    def destCity(self, paths: List[List[str]]) -> str:
        city = collections.Counter()

        for right in paths:
            city[right[0]] += 1
            city[right[1]] += 0

        for pair in city:
            if city[pair] == 0:
                return pair
        
        return ""
