class Solution:
    def reverseDegree(self, s: str) -> int:
        total_degree = 0
        
        for i, char in enumerate(s):
            reversed_weight = 123 - ord(char)
            position = i + 1
            
            total_degree += reversed_weight * position
            
        return total_degree