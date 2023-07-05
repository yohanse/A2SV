from collections import deque

def is_valid_bfs(n, tree_edges, sequence):
    # Create adjacency list representation of the tree
    graph = [[] for _ in range(n + 1)]
    for u, v in tree_edges:
        graph[u].append(v)
        graph[v].append(u)

    # Initialize a queue with vertex 1
    queue = deque([1])
    # Mark vertex 1 as used
    used = [False] * (n + 1)
    used[1] = True
    
    # Index to track position in given sequence
    seq_index = 0
    
    # Perform BFS
    while queue:
        # Extract vertex v from the head of the queue
        v = queue.popleft()

        # Compare with current element of sequence
        if v != sequence[seq_index]:
            return False
        seq_index += 1

        # All neighbors to be processed before moving to next level
        cnt = 0
        for u in graph[v]:
            if not used[u]:
                # Mark neighbor as used
                used[u] = True
                # Insert into queue
                queue.append(u)
                cnt += 1

        # Check if neighbors match with segment of sequence
        while cnt > 0:
            if seq_index >= len(sequence) or used[sequence[seq_index]] or sequence[seq_index] not in graph[v]:
                return False
            seq_index += 1
            cnt -= 1

    # If we have traversed through all elements of sequence, it's valid
    return seq_index == len(sequence)

# Example:
# Graph as adjacency list {1: [2, 3], 2: [4, 5]}
# Test if [1, 2, 3, 4, 5] is a valid BFS sequence
n = 5  # Number of vertices
tree_edges = []  # Edges of the tree


# Call function to check if sequence is valid BFS
n = int(input())
for i in range(n - 1):
    tree_edges.append(tuple(map(int, input().split())))
sequence = list(map(int, input().split()))

    
print(is_valid_bfs(n, tree_edges, sequence))  # Output: True