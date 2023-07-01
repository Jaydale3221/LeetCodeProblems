class Solution:
    def isPathCrossing(self, path: str) -> bool:
        # Set to store the coordinates
        coordinates = [(0, 0)]
        current_row, current_col = 0, 0

        # Iterate through each character in the path
        for direction in path:
            # Update the current row and column based on the direction
            match direction:
                case 'N':
                    current_col += 1
                case 'S':
                    current_col -= 1
                case 'E':
                    current_row += 1
                case 'W':
                    current_row -= 1

            # Check if the current coordinates have been visited before
            if (current_row, current_col) in coordinates:
                return True
            else: 
                coordinates.append((current_row, current_col))

        return False
