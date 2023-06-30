class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        counts = collections.Counter(magazine)  # Count the frequency of each character in the magazine
        for i in range(len(ransomNote)):
            if counts[ransomNote[i]] <= 0:  # If the count of a character in the ransom note is zero or negative, it cannot be formed
                return False
            
            counts[ransomNote[i]] -= 1  # Decrement the count of the character used from the magazine
        return True  # All characters in the ransom note can be formed using the magazine
