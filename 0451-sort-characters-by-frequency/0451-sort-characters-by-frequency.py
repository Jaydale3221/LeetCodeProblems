class Solution:
    def frequencySort(self, s: str) -> str:
        counts = collections.Counter(s)

        buckets = [[] for i in range(len(s) + 1)]

        answer = []
        for count in counts:
            buckets[counts[count]].append(count * counts[count])

        for i in range(len(buckets) - 1, 0 ,-1):
            for c in buckets[i]:
                answer.append(c)
            
        return "".join(answer)