class Solution:
    def maxSumOfSquares(self, num: int, sum: int) -> str:
        if sum > 9 * num:
            return ""
            
        nines = sum // 9
        remainder = sum % 9

        zeros = num - nines - (1 if remainder > 0 else 0)
        
        ans = []
        if nines > 0:
            ans.append("9" * nines)
            
        if remainder > 0:
            ans.append(str(remainder))
            
        if zeros > 0:
            ans.append("0" * zeros)
            
        return "".join(ans)