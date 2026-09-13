class Solution:
    def largestOverlap(self, img1: List[List[int]], img2: List[List[int]]) -> int:
        n = len(img1)
        ones1 = [(r, c) for r in range(n) for c in range(n) if img1[r][c] == 1]
        ones2 = [(r, c) for r in range(n) for c in range(n) if img2[r][c] == 1]
        
        if not ones1 or not ones2:
            return 0
            
        overlap_counts = defaultdict(int)
        max_overlap = 0
        
        for r1, c1 in ones1:
            for r2, c2 in ones2:
                shift_vec = (r2 - r1, c2 - c1)
                overlap_counts[shift_vec] += 1
                if overlap_counts[shift_vec] > max_overlap:
                    max_overlap = overlap_counts[shift_vec]
                    
        return max_overlap