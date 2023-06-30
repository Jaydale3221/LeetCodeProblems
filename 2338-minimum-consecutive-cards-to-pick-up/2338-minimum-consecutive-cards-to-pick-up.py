class Solution:
    def minimumCardPickup(self, cards: List[int]) -> int:
        last_seen = {}  # A dictionary to store the last seen index of each card
        min_distance = float('inf')  # Initialize the minimum distance with positive infinity

        for i in range(len(cards)):
            if cards[i] in last_seen:
                # Calculate the distance between the current index and the last seen index of the card
                distance =  i - last_seen[cards[i]] + 1 # Right - left + 1 

                min_distance = min(min_distance, distance)  # Update the minimum distance if necessary
            last_seen[cards[i]] = i  # Update the last seen index of the card
           

        # If a valid minimum distance is found, return it; otherwise, return -1
        return min_distance if min_distance != float('inf') else -1
