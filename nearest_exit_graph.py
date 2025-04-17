from collections import deque, defaultdict

class Solution:
    def nearestExit(self, maze: list[list[str]], entrance: list[int]) -> int:
        rows = len(maze)
        cols = len(maze[0])
        start_node = tuple(entrance)

        graph = defaultdict(list)
        directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]

        # iterando cada nó (row e column) para criar o grafo que contém apenas caminhos e não tem paredes
        for r in range(rows):
            for c in range(cols):
                # se for caminho, checa os vizinhos e adiciona na lista de adjacencia
                if maze[r][c] == '.':
                    current_node = (r, c)

                    for dr, dc in directions:
                        nr, nc = r + dr, c + dc

                        if 0 <= nr < rows and 0 <= nc < cols and maze[nr][nc] == '.':
                            neighbor_node = (nr, nc)
                            graph[current_node].append(neighbor_node)

        # coloca entrada na fila e marca como visitada
        queue = deque([(start_node, 0)])
        visited = {start_node}

        # algoritimo bfs usando fila
        while queue:
            current_node, steps = queue.popleft()
            r, c = current_node

            is_border = (r == 0 or r == rows - 1 or c == 0 or c == cols - 1)
            if current_node != start_node and is_border:
                return steps

            for neighbor_node in graph.get(current_node, []):
                if neighbor_node not in visited:
                    visited.add(neighbor_node)
                    queue.append((neighbor_node, steps + 1))

        return -1