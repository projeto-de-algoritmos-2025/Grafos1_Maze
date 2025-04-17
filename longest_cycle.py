from collections import defaultdict

class Solution:
    def longestCycle(self, edges: list[int]) -> int:
        n = len(edges)
        adj = defaultdict(list)
        for i, neighbor in enumerate(edges):
            if neighbor != -1:
                adj[i].append(neighbor)

        max_cycle_length = -1
        visited = [False] * n
        recursion_stack = [False] * n

        def dfs(node, path, path_nodes):
            nonlocal max_cycle_length
            visited[node] = True
            recursion_stack[node] = True
            path[node] = len(path)
            path_nodes.append(node)

            for neighbor in adj[node]:
                if not visited[neighbor]:
                    dfs(neighbor, path, path_nodes)
                elif recursion_stack[neighbor]:
                    # ciclo detectado
                    cycle_length = path[node] - path[neighbor] + 1
                    max_cycle_length = max(max_cycle_length, cycle_length)

            recursion_stack[node] = False
            path_nodes.pop()

        for i in range(n):
            if not visited[i]:
                dfs(i, {}, [])

        return max_cycle_length