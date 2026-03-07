# URL
https://adventofcode.com/2016/day/22

# Description
You gain access to a massive storage cluster arranged in a grid; each storage node is only connected to the four nodes directly adjacent to it (three if the node is on an edge, two if it's in a corner).

You can directly access data only on node /dev/grid/node-x0-y0, but you can perform some limited actions on the other nodes:

- You can get the disk usage of all nodes (via df). The result of doing this is in your puzzle input.
- You can instruct a node to move (not copy) all of its data to an adjacent node (if the destination node has enough space to receive the data). The sending node is left empty after this operation.
Nodes are named by their position: the node named node-x10-y10 is adjacent to nodes node-x9-y10, node-x11-y10, node-x10-y9, and node-x10-y11.

Before you begin, you need to understand the arrangement of data on these nodes. Even though you can only move data between directly connected nodes, you're going to need to rearrange a lot of the data to get access to the data you need. Therefore, you need to work out how you might be able to shift data around.

To do this, you'd like to count the number of viable pairs of nodes. A viable pair is any two nodes (A,B), regardless of whether they are directly connected, such that:

- Node A is not empty (its Used is not zero).
- Nodes A and B are not the same node.
- The data on node A (its Used) would fit on node B (its Avail).
How many viable pairs of nodes are there?

# Method of Solve
- The Part 01 of this challenge can be solved using the following code:
  ```
    import re
    
    def parse_nodes(filename):
        nodes = []
    
        with open(filename, "r") as f:
            for line in f:
                if line.startswith("/dev/grid"):
                    nums = list(map(int, re.findall(r"\d+", line)))
    
                    # nums = [x, y, size, used, avail, percent]
                    x, y, size, used, avail, percent = nums
    
                    nodes.append((used, avail))
    
        return nodes
    
    
    def count_viable_pairs(filename):
        nodes = parse_nodes(filename)
        count = 0
    
        for i in range(len(nodes)):
            usedA, availA = nodes[i]
    
            if usedA == 0:
                continue
    
            for j in range(len(nodes)):
                if i == j:
                    continue
    
                usedB, availB = nodes[j]
    
                if usedA <= availB:
                    count += 1
    
        return count
    
    
    if __name__ == "__main__":
        result = count_viable_pairs("input_22")
        print("Viable pairs:", result)
  ```
- This Solves the Part 01 of this challenge.
