class Solution:
    def destCity(self, paths: List[List[str]]) -> str:
        # Create a counter to keep track of cities
        city_counter = collections.Counter()

        # Iterate through each pair of cities in the paths
        for pair in paths:
            # Increment the count for the starting city
            city_counter[pair[0]] += 1
            city_counter[pair[1]] += 0

            # Initialize the count for the destination city (no need to increment)

        # Iterate through the cities in city_counter
        for city in city_counter:
            # If the count for a city is 0, it means it is a destination city
            if city_counter[city] == 0:
                return city

        # If no destination city is found, return an empty string
        return ""
