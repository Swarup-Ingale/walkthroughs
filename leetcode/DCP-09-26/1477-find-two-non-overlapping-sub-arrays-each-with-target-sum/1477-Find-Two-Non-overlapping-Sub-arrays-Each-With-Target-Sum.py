class Solution:
    def minSumOfLengths(self, arr: list[int], target: int) -> int:
        n = len(arr)
        min_len = [float('inf')] * n
        ans = float('inf')
        
        left = 0
        curr_sum = 0
        
        for right in range(n):
            curr_sum += arr[right]
            
            while curr_sum > target and left <= right:
                curr_sum -= arr[left]
                left += 1
                
            current_best = float('inf')

            if curr_sum == target:
                l = right - left + 1

                if left > 0 and min_len[left - 1] != float('inf'):
                    ans = min(ans, l + min_len[left - 1])
                    
                current_best = l

            if right > 0:
                min_len[right] = min(min_len[right - 1], current_best)
            else:
                min_len[right] = current_best
                
        return ans if ans != float('inf') else -1