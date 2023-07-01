class Solution:
    def frequencySort(self, s: str) -> str:
        counts = collections.Counter(s)
        answer = []
        buckets = [[] for i in range(len(s) + 1)]

        for count in counts:
            buckets[counts[count]].append(counts[count] * count)

        for i in range(len(buckets) -1, 0 , -1):
            for c in buckets[i]: #index of buckets
                answer.append(c)
        
        return "".join(answer)

 
