class Solution:
    def robotWithString(self, s: str) -> str:
        counts = collections.Counter(s)
        t, answer = [], []
        
        for character in s:
            t.append(character)

            if counts[character] == 1:
                del counts[character]
            else:
                counts[character] -= 1
            
            while t and counts and min(counts) >= t[-1]:
                answer.append(t.pop())
        
        while t:
            answer.append(t.pop())
        
        return "".join(answer)
