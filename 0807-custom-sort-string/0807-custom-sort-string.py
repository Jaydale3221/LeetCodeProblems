class Solution:
    def customSortString(self, order: str, s: str) -> str:
        count = collections.Counter(s)
        answer = []
        for i in order:
            answer.append(i * count[i])
            # count[i] = 0
            del count[i]
        
        for i in count:
            answer.append(i * count[i])
        
        return "".join(answer)
