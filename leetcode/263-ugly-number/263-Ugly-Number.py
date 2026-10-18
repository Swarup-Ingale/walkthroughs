class Solution:
    def isUgly(self, n: int) -> bool:
        if n <= 0:
            return False
        max_ugly_32bit = 2**30 * 3**19 * 5**13 
    
        if n == 1:
            return True
        if n % 2 == 0:
            return self.isUgly(n // 2)
        if n % 3 == 0:
            return self.isUgly(n // 3)
        if n % 5 == 0:
            return self.isUgly(n // 5)
            
        return False