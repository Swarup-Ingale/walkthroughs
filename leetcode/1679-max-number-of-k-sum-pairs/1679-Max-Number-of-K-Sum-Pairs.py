class Solution:
    def maxOperations(self, nums: List[int], k: int) -> int:
        seen = defaultdict(int)
        operations = 0
        
        for num in nums:
            complement = k - num

            if seen[complement] > 0:
                operations += 1
                seen[complement] -= 1
            else:
                seen[num] += 1
                
        return operations