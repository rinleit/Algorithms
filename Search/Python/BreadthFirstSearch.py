from queue import Queue

class BreadthFirstSearch:

    def bfs(self, graph, start, end):
        queue = Queue()
        path = [start]
        queue.put(path)
        visited = set([start])

        while not queue.empty():
            path = queue.get()
            last = path[-1]
            if last == end:
                return path
            for node in graph[last]:
                if node not in visited:
                    visited.add(node)
                    queue.put(path + [node])


if __name__ == '__main__':
    bfs = BreadthFirstSearch()
    graph = {1: [2, 3],
             2: [1, 4, 6],
             3: [1, 4],
             4: [2, 3, 5],
             5: [2, 4, 6],
             6: [2, 5, 9]}
    print("DFS: ", bfs.bfs(graph, 1, 6))
