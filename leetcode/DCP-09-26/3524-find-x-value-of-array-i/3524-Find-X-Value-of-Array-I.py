class Solution:
    def resultArray(self, nums: List[int], k: int) -> List[int]:
        result = [0] * k
        current_counts = [0] * k
        
        for num in nums:
            next_counts = [0] * k
            val = num % k

            next_counts[val] += 1

            for r in range(k):
                if current_counts[r] > 0:
                    new_r = (r * val) % k
                    next_counts[new_r] += current_counts[r]

            for r in range(k):
                result[r] += next_counts[r]

            current_counts = next_counts
            
        return result