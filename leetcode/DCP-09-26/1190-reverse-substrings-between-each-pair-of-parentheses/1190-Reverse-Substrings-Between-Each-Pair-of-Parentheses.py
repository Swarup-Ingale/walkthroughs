class Solution:
    def reverseParentheses(self, s: str) -> str:
        n = len(s)
        open_parantheses = []
        pair = [0] * n

        for i in range(n):
            if s[i] == "(":
                open_parantheses.append(i)
            if s[i] == ")":
                j = open_parantheses.pop()
                pair[i] = j
                pair[j] = i

        r = []
        curr_idx = 0
        direction = 1
        
        while curr_idx < n:
            if s[curr_idx] == "(" or s[curr_idx] == ")":
                curr_idx = pair[curr_idx]
                direction = -direction
            else:
                r.append(s[curr_idx])
            curr_idx += direction
        
        return "".join(r)

# The "Wormhole" Pattern Explained

# What is it?

# Normally, solving this problem requires a Stack where you physically pull strings out, reverse them, and put them back in. 
# In a heavily nested string like ((((a)))), physically reversing the inner strings over and over again causes the time complexity to degrade to $\mathcal{O}(N^2)$.
# The Wormhole pattern prevents this by treating parentheses as teleportation portals. Instead of physically reversing the string in memory, you simply walk backwards.

# How it works:
# 1. Link the Portals: First, map every ( to its matching ) so they know about each other.
# 2. Walk the String: Start walking left to right (direction = 1).
# 3. Teleport and Flip: When you hit a parenthesis, you jump immediately to its partner. 

# Because you just entered a nested layer (which is supposed to be reversed), you just flip your walking direction (direction = -direction) and keep collecting characters.

# When to use it:

# Use this pattern whenever a problem asks you to repeatedly reverse nested structures, simulate paths bouncing between mirrors, or navigate linked nodes that change directions. 
# It transforms an $\mathcal{O}(N^2)$ physical simulation into an $\mathcal{O}(N)$ graph-traversal problem.
