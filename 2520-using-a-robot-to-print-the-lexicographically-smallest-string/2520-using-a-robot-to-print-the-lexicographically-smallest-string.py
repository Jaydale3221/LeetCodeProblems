class Solution:
    def robotWithString(self, s: str) -> str:
        counts = collections.Counter(s)
        answer, t = [], []
        for char in s:
            t.append(char)
            if counts[char] == 1:
                del counts[char]
            else:
                counts[char] -= 1
            while t and counts and min(counts) >= t[-1]:
                answer.append(t.pop())
        while t:
            answer.append(t.pop())
        
        return "".join(answer)
        
        