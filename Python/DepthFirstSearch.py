class DepthFirstSearch:

    def dfs(self, graph, start):
        stack = [start]
        path = []
        while not stack.isEmpty:
            vertex = stack.pop()
            if vertex not in path:
                path.append(vertex)
            for node in reversed(graph[vertex]):
                if node not in path:
                    stack.append(node)
        return path

    def dfs_recursive(self, graph, start, path = []):
        path.append(start)
        for edge in graph[start]:
            if edge not in path:
                path = self.dfs_recursive(graph, edge, path)
        return path

if __name__ == '__main__':
    dfs = DepthFirstSearch()
    graph = {1: [2, 3],
             2: [1, 4, 6],
             3: [1, 4],
             4: [2, 3, 5],
             5: [2, 4, 6],
             6: [2, 5, 9]}
    print("DFS: ", dfs.dfs(graph, 1))
    print("DFS recursive: ", dfs.dfs_recursive(graph, 1))
