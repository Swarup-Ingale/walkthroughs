import sys
from typing import List

class Solution:
    def resultArray(self, nums: List[int], k: int, queries: List[List[int]]) -> List[int]:
        sys.setrecursionlimit(200000)
        
        n = len(nums)
        tree_prod = [1] * (4 * n)
        tree_counts = [[0] * k for _ in range(4 * n)]
        
        def build(node: int, start: int, end: int):
            if start == end:
                v = nums[start] % k
                tree_prod[node] = v
                tree_counts[node][v] = 1
                return
            
            mid = (start + end) // 2
            left = 2 * node
            right = 2 * node + 1
            
            build(left, start, mid)
            build(right, mid + 1, end)

            tree_prod[node] = (tree_prod[left] * tree_prod[right]) % k
            
            for i in range(k):
                tree_counts[node][i] = tree_counts[left][i]
                
            left_prod = tree_prod[left]
            for i in range(k):
                if tree_counts[right][i] > 0:
                    new_val = (left_prod * i) % k
                    tree_counts[node][new_val] += tree_counts[right][i]
                    
        def update(node: int, start: int, end: int, idx: int, val: int):
            if start == end:
                v = val % k
                tree_prod[node] = v
                for i in range(k):
                    tree_counts[node][i] = 0
                tree_counts[node][v] = 1
                return
            
            mid = (start + end) // 2
            left = 2 * node
            right = 2 * node + 1
            
            if idx <= mid:
                update(left, start, mid, idx, val)
            else:
                update(right, mid + 1, end, idx, val)

            tree_prod[node] = (tree_prod[left] * tree_prod[right]) % k
            
            for i in range(k):
                tree_counts[node][i] = tree_counts[left][i]
                
            left_prod = tree_prod[left]
            for i in range(k):
                if tree_counts[right][i] > 0:
                    new_val = (left_prod * i) % k
                    tree_counts[node][new_val] += tree_counts[right][i]
                    
        def query(node: int, start: int, end: int, ql: int, qr: int):
            if ql <= start and end <= qr:
                return tree_prod[node], tree_counts[node]
            
            mid = (start + end) // 2
            
            if qr <= mid:
                return query(2 * node, start, mid, ql, qr)
            elif ql > mid:
                return query(2 * node + 1, mid + 1, end, ql, qr)

            l_prod, l_counts = query(2 * node, start, mid, ql, qr)
            r_prod, r_counts = query(2 * node + 1, mid + 1, end, ql, qr)
            
            res_prod = (l_prod * r_prod) % k
            res_counts = [0] * k
            
            for i in range(k):
                res_counts[i] = l_counts[i]
                
            for i in range(k):
                if r_counts[i] > 0:
                    new_val = (l_prod * i) % k
                    res_counts[new_val] += r_counts[i]
                    
            return res_prod, res_counts

        build(1, 0, n - 1)
        
        result = []

        for idx, val, start_idx, x in queries:
            update(1, 0, n - 1, idx, val)

            _, counts = query(1, 0, n - 1, start_idx, n - 1)

            result.append(counts[x])
            
        return result