class Solution:
    def sortableIntegers(self, nums: list[int]) -> int:
        n = len(nums)
        sorted_nums = sorted(nums)

        divisors = []
        for i in range(1, int(n**0.5) + 1):
            if n % i == 0:
                divisors.append(i)
                if i * i != n:
                    divisors.append(n // i)
                    
        ans = 0

        for k in divisors:
            possible = True

            for j in range(0, n, k):
                B = nums[j : j+k]
                G = sorted_nums[j : j+k]

                drops = [i for i in range(k - 1) if B[i] > B[i+1]]
                
                if len(drops) > 1:
                    possible = False
                    break
                elif len(drops) == 1:
                    d = drops[0]
                    if B[d+1:] + B[:d+1] != G:
                        possible = False
                        break
                else:
                    if B != G:
                        possible = False
                        break
                        
            if possible:
                ans += k
                
        return ans