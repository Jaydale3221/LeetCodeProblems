class Solution(object):
    def numJewelsInStones(self, J, S):
        Jset = set(J)  # Create a set of unique characters from the string J (representing types of jewels)
        return sum(s in Jset for s in S)  # Count the number of stones (characters in S) that are also present in the set of jewels (Jset)
