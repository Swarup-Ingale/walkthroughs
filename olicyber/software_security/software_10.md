# URL
https://training.olicyber.it/challenges#challenge-264

# Concept
`ltrace` can be noisy when a binary makes many library calls. The `-e` option filters the output to only show calls to specified function(s), making it easy to focus on the relevant call (e.g., `access`).

# Method of Solve
1. **Run with ltrace filtering for `access`**:
   ```
   ltrace -e access ./sw-10
   ```
2. **Observe filtered output**:
   ```
   sw-10->access("flag{0f32826c}", 0) = -1
   ```

# Flag
`flag{0f32826c}`
- So the Final Flag is **flag{0f32826c}**
